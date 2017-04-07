import urwid
import datetime
from bundle import Bundle

POST_LIST_STATUS = {
    'WaitingForCrawling': 'WaitingForCrawling',
    'WaitingForRender': 'WaitingForRender'
}

class App(object):
    """Docstring for App."""
    def __init__(self):
        super(App, self).__init__()
        self.bundle = Bundle()
        self.app = urwid.MainLoop(self.bundle.output, unhandled_input=self.bundle.globle_input_listener)
        self.signal_flash = True
        self.app.set_alarm_in(1, self.update_datetime)
        self.app.set_alarm_in(0.5, self.post_list_status_tracker)
        self.app.run()

    def update_datetime(self, loop, *args):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.bundle.header.datetime.set_text(str(now))
        self.app.set_alarm_in(1, self.update_datetime)

    def post_list_status_tracker(self, loop, *args):
        if self.bundle.body.post_list.status == POST_LIST_STATUS['WaitingForCrawling']:
            self.bundle.body.post_list.crawl_posts()
        if self.bundle.body.post_list.status == POST_LIST_STATUS['WaitingForRender']:
            self.bundle.body.post_list.render()
        self.app.set_alarm_in(0.1, self.post_list_status_tracker)
