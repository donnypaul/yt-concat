import os
from yt_concat.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Running postflight')
        if inputs['cleanup']:
            utils.remove_dirs()

