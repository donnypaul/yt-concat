import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound
from yt_concat.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exists(url):
                print('Found existing caption file')
                continue
            try:
                captions = YouTubeTranscriptApi.get_transcript(utils.get_video_id(url))
                captions = str(captions)

            except (TranscriptsDisabled, NoTranscriptFound):
                print('English subtitles are not available for', url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(captions)
            text_file.close()
        end = time.time()
        print('It took', end - start, 'seconds to download all caption files')
        return data

