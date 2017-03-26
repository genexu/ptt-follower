import urwid
from bundle import Bundle

bundle = Bundle()

def run():
    app = urwid.MainLoop(bundle.output, unhandled_input=bundle.globle_input_listener)
    app.run()
