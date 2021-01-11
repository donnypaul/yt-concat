import os
from yt_concat.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Running postflight')
        if inputs['cleanup']:
            # for found in data:
            #     filepath = utils.get_video_filepath(found.yt.id)
            #     filepath.close()
            utils.remove_dirs()

