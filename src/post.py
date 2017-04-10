class Post(object):
    """Docstring for Post."""
    def __init__(self, title, author, date, url, timesteap):
        super(Post, self).__init__()
        self.title = title
        self.author = author
        self.date = date
        self.url = url
        self.timesteap = timesteap
