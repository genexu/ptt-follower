import urwid

class Body(object):
    """Docstring For Body."""
    def __init__(self):
        super(Body, self).__init__()

    def render(self):
        body_txt = urwid.Text(u"Body", align='center')
        return urwid.Filler(body_txt, valign='middle')
