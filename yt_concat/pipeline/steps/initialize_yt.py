from yt_concat.pipeline.steps.step import Step
from yt_concat.model.yt import YT

class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]