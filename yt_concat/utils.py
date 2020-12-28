import os

from yt_concat.settings import CAPTIONS_DIR
from yt_concat.settings import VIDEOS_DIR
from yt_concat.settings import DOWNLOADS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        filepath = self.get_video_list_filepath(channel_id)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_caption_filepath(self, yt):
        return os.path.join(CAPTIONS_DIR, yt.url + '.txt')

    def caption_file_exists(self, url):
        filepath = self.get_caption_filepath(url)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_video_filepath(self, yt):
        return os.path.join(VIDEOS_DIR, yt.url)