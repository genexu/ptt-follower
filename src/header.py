import urwid
import datetime

class Header(object):
    """Docstring For Header."""
    def __init__(self):
        super(Header, self).__init__()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = urwid.Text(u"PTT FOLLOWER", align='left')
        self.datetime = urwid.Text(str(now), align='right')
        self.output = urwid.Columns([ self.title, self.datetime ])
