from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id()
        self.captions = self.get_video_captions()  #All captions in a video

    def get_video_id(self):
        return self.url.split('watch?v=')[-1]

    def get_video_captions(self):
        try:
            return YouTubeTranscriptApi.get_transcript(self.id)

        except (TranscriptsDisabled, NoTranscriptFound):
            print('English subtitles are not available for', self.url)
            return 0
