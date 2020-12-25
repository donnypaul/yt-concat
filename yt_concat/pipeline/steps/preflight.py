from yt_concat.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('Running preflight')
        utils.create_dirs()