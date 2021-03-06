import urwid

DESC = 'DESC'
ADD_NEW_ID = 'ADD_NEW_ID'
ADD_NEW_BOARD = 'ADD_NEW_BOARD'
DEFAULT_DESC = '(I)Add Id (B)Add Board (N)Edit Crawl Number Of Page (D)Delete Board/Id (R)Reload (q/Q)Exit'
DEFAULT_RESPONSE = 'None'

class Footer(object):
    """Docstring for Footer."""
    def __init__(self, desc=DEFAULT_DESC, input_response=DEFAULT_RESPONSE):
        super(Footer, self).__init__()
        self.desc_text = urwid.Text(desc, align='left')
        self.input_response_text = urwid.Text('Response Input: %s' %(repr(input_response)), align='right')
        self.output = urwid.Columns(self.generate(DESC))

    def generate(self, mode):
        if mode == DESC:
            return [ self.desc_text, self.input_response_text ]
        if mode == ADD_NEW_ID:
            return [urwid.Edit(u"Id: "), urwid.Text(u"(Esc) Exit Add Mode", align='right')]
        if mode == ADD_NEW_BOARD:
            return [urwid.Edit(u"Board: "), urwid.Text(u"(Esc) Exit Add Mode", align='right')]

    def desc(self):
        self.contents_replace(self.generate(DESC))

    def add_new_id(self):
        self.contents_replace(self.generate(ADD_NEW_ID))

    def add_new_board(self):
        self.contents_replace(self.generate(ADD_NEW_BOARD))

    def delete_id(self, index):
        content = [urwid.Edit(u"Delete Id [%s](y/n): " % index), urwid.Text(u"(Esc) Exit Delete Mode", align='right')]
        self.contents_replace(content)

    def delete_board(self, index):
        content = [urwid.Edit(u"Delete Board [%s](y/n): " % index), urwid.Text(u"(Esc) Exit Delete Mode", align='right')]
        self.contents_replace(content)

    def update_crawl_number_of_page(self, n):
        edit = urwid.Edit(u"Crawl Number Of Page: ")
        edit.set_edit_text(str(n))
        text = urwid.Text(u"(Esc) Exit Edit Mode", align='right')
        content = [edit, text]
        self.contents_replace(content)

    def contents_replace(self, contents):
        self.output.contents = []
        for c in contents:
            self.output.contents.append((c, self.output.options()))

    def input_response(self, key):
        self.input_response_text.set_text('Response Input: %s' %(repr(key)))
