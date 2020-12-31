import time
import concurrent.futures
from pytube import YouTube
from yt_concat.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        video_links = []
        video_ids = []
        for found in data:
            url = found.yt.url
            video_id = found.yt.id
            if utils.video_file_exists(url):
                print(f'found video {video_id}.mp4')
                continue
            video_links.append(url)
            video_ids.append(video_id)

        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for video in executor.map(self.download, video_links, video_ids):
                print('downloading:', video)
        end = time.time()
        print('It took', (end - start) / 60, 'minutes to download all videos.')
        return data

    @staticmethod
    def download(url, video_id):
        return YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=video_id)



