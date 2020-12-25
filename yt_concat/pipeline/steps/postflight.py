from yt_concat.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('Running postflight')
