from pytube import YouTube
from yt_concat.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        for found in data:
            url = found.yt.url
            video_id = found.yt.id
            if utils.video_file_exists(url):
                print(f'found video {video_id}.mp4')
                continue
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=video_id)
        return data

