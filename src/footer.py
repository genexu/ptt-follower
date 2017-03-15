import urwid

class Footer(object):
    """Docstring for Footer."""
    def __init__(self, desc="Default Desc", input_response="None"):
        super(Footer, self).__init__()
        self.desc_text = urwid.Text(desc, align='left')
        self.input_response_text = urwid.Text('Response Input: %s' %(repr(input_response)), align='right')

    def render(self):
        return urwid.Columns([self.desc_text, self.input_response_text])

    def input_response(self, key):
        self.input_response_text.set_text('Response Input: %s' %(repr(key)))
