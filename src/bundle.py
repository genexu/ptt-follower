import urwid
from header import Header
from body import Body
from footer import Footer

NORMAL = 'NORMAL'
ADD_NEW_ID = 'ADD_NEW_ID'
ADD_NEW_BOARD = 'ADD_NEW_BOARD'

class Bundle(object):
    """docstring for Bundle."""
    def __init__(self):
        super(Bundle, self).__init__()
        self.header = Header()
        self.body = Body()
        self.footer = Footer()
        self.status = NORMAL
        self.output = urwid.Frame(self.body.render(), header=self.header.render(), footer=self.footer.render(), focus_part='body')

    def render(self):
        return self.output

    def globle_input_listener(self, key):
        self.footer.input_response(key)
        if key in ('I'):
            self.status = ADD_NEW_ID
            self.footer.add_new_id()
            self.output.focus_position = 'footer'

        if key in ('B'):
            self.status = ADD_NEW_BOARD
            self.footer.add_new_board()
            self.output.focus_position = 'footer'

        if key in ('esc'):
            if self.status in (ADD_NEW_ID, ADD_NEW_BOARD):
                self.status = NORMAL
                self.footer.desc()
                self.output.focus_position = 'body'

        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
