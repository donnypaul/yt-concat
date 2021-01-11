import urllib.request
import json
from yt_concat.settings import API_KEY
from yt_concat.pipeline.steps.step import Step
from yt_concat.pipeline.steps.step import StepException


class GetVideoList(Step):

    def process(self, data, inputs, utils, logger):
        channel_id = inputs['channel_id']
        fast = inputs['fast']
        if utils.video_list_file_exists(channel_id) and fast:
            logger.info(f'Found video list file for channel ID: {channel_id}')
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    @staticmethod
    def write_to_file(video_link, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for url in video_link:
                f.write(url + '\n')

    @staticmethod
    def read_file(filepath):
        video_link = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for url in f:
                video_link.append(url.strip())
        return video_link

