class SongMeta():
    def __init__(self, **kwargs):
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.artist = kwargs['artist'] if 'artist' in kwargs else None
        self.music = kwargs['music'] if 'music' in kwargs else None
        self.lyrics = kwargs['lyrics'] if 'lyrics' in kwargs else None
        self.arranged = kwargs['arranged'] if 'arranged' in kwargs else None
        self.album = kwargs['album'] if 'album' in kwargs else None
        self.year = kwargs['year'] if 'year' in kwargs else None
        self.tempo = kwargs['tempo'] if 'tempo' in kwargs else None
        self.key = kwargs['key'] if 'key' in kwargs else None
        self.mode = kwargs['mode'] if 'mode' in kwargs else None
        self.comments = kwargs['comments'] if 'comments' in kwargs else None
