from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.utils import Utils
from yt_concat.pipeline.steps.preflight import Preflight
from yt_concat.pipeline.steps.postflight import Postflight
from yt_concat.pipeline.steps.get_video_list import GetVideoList
from yt_concat.pipeline.steps.download_captions import DownloadCaptions


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'CHANNEL_ID': CHANNEL_ID,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()