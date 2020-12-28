from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.utils import Utils
from yt_concat.pipeline.steps.preflight import Preflight
from yt_concat.pipeline.steps.get_video_list import GetVideoList
from yt_concat.pipeline.steps.initialize_yt import InitializeYT
from yt_concat.pipeline.steps.search import Search
from yt_concat.pipeline.steps.postflight import Postflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'CHANNEL_ID': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        Search(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()