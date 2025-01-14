import asyncio
from soundcloud import SoundCloud
from soundcloud.resource.track import Track
from soundcloud.resource.user import User
from soundcloud.resource.playlist import AlbumPlaylist



from typing import Union
import itertools
import subprocess, aiohttp, aiofiles
import tempfile, eyed3
import math
from logging import Logger

from .util import clean_filename
from .util import apply_tags 





class Sound_Cloud:
    def __init__(self, client_id:str, auth_token:str, 
                 loop:asyncio.BaseEventLoop, executor=None, logger:Logger=None) -> None:
        
        self.sc_client = SoundCloud(client_id = client_id, 
                                    auth_token = auth_token)
        
        self.loop = loop
        self.logger = logger
        self.executor = executor
        self.available_filters = ['track', 'user', 'album', 'playlist']
        self.methods = [
            'get_track',
            'download'
        ]


    async def __search_api_query(self, query:str,  filter:str, limit:int) -> Union[Track, User, AlbumPlaylist]:
        if filter == "track":
            data = self.sc_client.search_tracks(query = query)
        elif filter == "user":
            data = self.sc_client.search_users(query = query)
        elif filter == "album":
            data = self.sc_client.search_albums(query = query)
        elif filter == "playlist":
            data = self.sc_client.search_playlists(query = query)

        limited_data = itertools.islice(data, limit)
        return limited_data
    async def __api_query(self, method:str, **kwargs):
        data = None
        if method in self.methods:
            if method == 'get_track':
                data = self.sc_client.get_track(kwargs.get('track_id', 0))
                
            elif method == 'download':
                track_id = kwargs.get('track_id', 0)
                path_to_file = kwargs.get('path_to_file', "./")

                if self.logger: self.logger.info(f'[SC-DL] [{track_id}]: Download start..')
                track = await self.get_track(track_id)
                file_name = clean_filename(f'{track.title} - {track.user.username}.mp3')
                file_path = path_to_file + file_name
                track_title = clean_filename(track.title)
                track_tags = {
                    'title': track_title,
                    'artist': track.user.username.encode("utf-8", "ignore").decode("utf-8"),
                    'album': track_title,
                    'cover': track.artwork_url
                }
                with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as temp_file:
                    temp_file_path = temp_file.name
                    download_url = None


                    if track.downloadable:
                        download_url = self.sc_client.get_track_original_download(track.id, track.secret_token)
                        
                    
                    if download_url:
                        async with aiohttp.ClientSession(headers=self.sc_client.get_default_headers()) as session:
                            async with session.get(download_url, params={"client_id": self.sc_client.client_id}) as response:
                                audio_data = await response.read()
                                async with aiofiles.open(temp_file_path, 'wb') as f:
                                    await f.write(audio_data)
                        p = subprocess.Popen(
                            ["ffmpeg", "-i", temp_file_path, "-loglevel", "error", "-vn", "-acodec", "libmp3lame", "-q:a", "0", file_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                        stdout, stderr = p.communicate()
                        if stderr and self.logger:
                            self.logger.error(f"[SC-DL] [{track_id}] ERROR: {stderr.decode('utf-8')}")
                        
                        if self.logger: self.logger.info(f'[SC-DL] [{track_id}]: Setting tags to an audio file..')
                        await apply_tags(file_path, track_tags)
                        data = file_path
                    else:
                        aac_transcoding = None
                        mp3_transcoding = None
                        
                        for t in track.media.transcodings:
                            if t.format.protocol == "hls" and "aac" in t.preset:
                                aac_transcoding = t
                            elif t.format.protocol == "hls" and "mp3" in t.preset:
                                mp3_transcoding = t

                        transcoding = None

                        if aac_transcoding:
                            transcoding = aac_transcoding
                        elif mp3_transcoding:
                            transcoding = mp3_transcoding


                        if not transcoding:
                            return None
                        
                        if self.logger: self.logger.info(f'[SC-DL] [{track_id}]: Download link generation..')
                        url = transcoding.url
                        bitrate_KBps = 256 / 8 if "aac" in transcoding.preset else 128 / 8
                        total_bytes = bitrate_KBps * transcoding.duration
                        
                        min_size = 0
                        max_size = math.inf
                        
                        if not min_size <= total_bytes <= max_size:
                            return None
                        
                        download_url = None
                        if url is not None:
                            headers = self.sc_client.get_default_headers()
                            if self.sc_client.auth_token:
                                headers["Authorization"] = f"OAuth {self.sc_client.auth_token}"

                            async with aiohttp.ClientSession(headers=headers) as session:
                                async with session.get(url, params={"client_id": self.sc_client.client_id}) as response:
                                    download_url = await response.json()

                        if download_url:
                            p = subprocess.Popen(
                                ["ffmpeg", "-i", download_url['url'], "-c", "copy", file_path, "-loglevel", "error", "-vn", "-acodec", "libmp3lame", "-q:a", "0"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE
                            )
                            stdout, stderr = p.communicate()
                            if stderr and self.logger:
                                self.logger.error(f"[SC-DL] [{track_id}] ERROR: {stderr.decode('utf-8')}")
                            
                            if self.logger: self.logger.info(f'[SC-DL] [{track_id}]: Setting tags to an audio file..')
                            await apply_tags(file_path, track_tags)
                            data = file_path
            return data


    async def download_track(self, track_id:int, path_to_file:str, **kwargs):
        """
            Downloading a track by its ID

            :param track_id: Track ID on SoundCloud
            :param path_to_file: The path where the file will be uploaded

            :return: String with file path
        """
        task = await self.loop.run_in_executor(self.executor, 
                    lambda: self.__api_query(
                                    method='download',
                                    track_id = track_id, path_to_file = path_to_file, **kwargs))
        
        
        task_result = await task
        return task_result
    async def get_track(self, track_id:int, **kwargs) -> Track:
        """
            Getting information from a track by its ID

            :param track_id: Track ID on SoundCloud

            :return: SoundCloud.BasicTrack 
        """
        task = await self.loop.run_in_executor(self.executor, 
                    lambda: self.__api_query(
                                    method='get_track',
                                    track_id = track_id,**kwargs))
        
        
        task_result = await task
        return task_result

    async def search(self, query:str, filter:str='track', limit:int=10):
        """
            Soundcloud search


            :param query: Search string
            :param filter: Filter for item types. Allowed values: ``track``, ``user``, ``album``, ``playlist``.
            Default: ``track``
            :param limit: Limit Results
            Default: ``10``

            :return: Generator limited by ``limit``
        """
        
        if filter not in self.available_filters:
            filter = self.available_filters[0]
        
        task = await self.loop.run_in_executor(self.executor, lambda: self.__search_api_query(query, filter, limit))
        task_result = await task
        return task_result