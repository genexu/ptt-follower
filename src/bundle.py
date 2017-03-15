import urwid
from header import Header
from body import Body
from footer import Footer

header = Header()
body = Body()
footer = Footer()

class Bundle(object):
    """docstring for Bundle."""
    def __init__(self):
        super(Bundle, self).__init__()

    def render(self):
        return urwid.Frame(body.render(), header=header.render(), footer=footer.render(), focus_part='body')

    def globle_input_listener(self, key):
        footer.input_response(key)
