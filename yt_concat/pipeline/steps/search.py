from .step import Step
from yt_concat.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils, logger):
        search_word = inputs['search_word']
        found = []
        for yt in data:
            if yt.captions == 0:
                continue
            for caption in yt.captions:
                if search_word in caption['text']:
                    f = Found(yt, caption)
                    found.append(f)
        # logger.info(found)
        return found
