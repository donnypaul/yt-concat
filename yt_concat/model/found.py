class Found:
    def __init__(self, url, captions):
        self.url = url
        self.captions = captions
        self.caption = captions['text']
        self.start_time = captions['start']
        self.end_time = captions['start'] + captions['duration']

    def __str__(self):
        return '<Found' + self.captions + '>'

    def __repr__(self):
        content = ':'.join([
            'yt= ' + str(self.url),
            'caption= ' + str(self.caption),
            'start_time= ' + str(self.start_time),
            'end_time= ' + str(self.end_time),
        ])
        return '<found ' + content + '>'

