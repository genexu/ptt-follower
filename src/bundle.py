import urwid
from header import Header
from body import Body
from footer import Footer

class Bundle(object):
    """docstring for Bundle."""
    def __init__(self):
        super(Bundle, self).__init__()
        self.header = Header()
        self.body = Body()
        self.footer = Footer()
    def render(self):
        return urwid.Frame(self.body.render(), header=self.header.render(), footer=self.footer.render(), focus_part='body')

    def globle_input_listener(self, key):
        self.footer.input_response(key)
