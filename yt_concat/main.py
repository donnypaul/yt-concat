import sys
import getopt
import logging
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.utils import Utils
from yt_concat.pipeline.steps.preflight import Preflight
from yt_concat.pipeline.steps.get_video_list import GetVideoList
from yt_concat.pipeline.steps.initialize_yt import InitializeYT
from yt_concat.pipeline.steps.search import Search
from yt_concat.pipeline.steps.download_videos import DownloadVideos
from yt_concat.pipeline.steps.edit_videos import EditVideos
from yt_concat.pipeline.steps.postflight import Postflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def print_usage():
    print('python main.py OPTIONS')
    print('OPTIONS:')
    print('{:>6} {:<17} {}'.format('-c', '--channel_id', 'Channel ID of your target youtube channel'))
    print('{:>6} {:<17} {}'.format('-s', '--search_word', 'The word that you want to capture in videos'))
    print('{:>6} {:<17} {}'.format('-l', '--limit', 'The maximum number of capture videos in the output video'))
    print('{:>6} {:<17} {}'.format('-g', '--logging_level', 'The logging level shown on the CMD screen. '
                                                            '[Fill a number only] '
                                                            '[1:DEBUG, 2:INFO, 3:WARNING, 4:ERROR, 5:CRITICAL]'))
    print('{:<24} {}'.format('cleanup', 'Remove all downloaded videos'))
    print('{:<24} {}'.format('fast', 'Skip downloading video list and videos if exist'))


def command_line_arg():
    channel_id = CHANNEL_ID
    search_word = 'incredible'
    limit = 30
    logging_level = logging.DEBUG
    cleanup = False
    fast = False
    short_opt = 'hc:s:l:g:'
    long_opt = 'help channel_id= search_word= limit= logging_level= cleanup fast'.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opt, long_opt)
        print(opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-c", "--channel_id"):
            channel_id = arg
        elif opt in ("-s", "--search_word"):
            search_word = arg
        elif opt in ("-l", "--limit"):
            limit = int(arg)
        elif opt in ("-g", "--logging_level"):
            if arg == '1':
                logging_level = logging.DEBUG
            elif arg == '2':
                logging_level = logging.INFO
            elif arg == '3':
                logging_level = logging.WARNING
            elif arg == '4':
                logging_level = logging.ERROR
            elif arg == '5':
                logging_level = logging.CRITICAL
        elif opt == '--cleanup':
            cleanup = True
        elif opt == '--fast':
            fast = True
    return channel_id, search_word, limit, logging_level, cleanup, fast


def config_logger(logging_level):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('yt_concat_logging.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def main():
    channel_id, search_word, limit, logging_level, cleanup, fast = command_line_arg()
    inputs = {
        'channel_id': channel_id,
        'search_word': search_word,
        'limit': limit,
        'logging_level': logging_level,
        'cleanup': cleanup,
        'fast': fast,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        Search(),
        DownloadVideos(),
        EditVideos(),
        Postflight(),
    ]

    logger = config_logger(logging_level)
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils, logger)


if __name__ == '__main__':
    main()