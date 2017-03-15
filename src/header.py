import urwid

class Header(object):
    """Docstring For Header."""
    def __init__(self):
        super(Header, self).__init__()

    def render(self):
        return urwid.Text(u"Header", align='center')
