import urwid
import datetime
from bundle import Bundle

class App(object):
    """Docstring for App."""
    def __init__(self):
        super(App, self).__init__()
        self.bundle = Bundle()
        self.app = urwid.MainLoop(self.bundle.output, unhandled_input=self.bundle.globle_input_listener)
        self.signal_flash = True
        self.app.set_alarm_in(1, self.update_datetime)
        self.app.run()

    def update_datetime(self, loop, *args):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.bundle.header.datetime.set_text(str(now))
        self.app.set_alarm_in(1, self.update_datetime)
