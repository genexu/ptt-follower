import urwid
from footer import Footer

footer = Footer()

def run():
    header = urwid.Text(u"Header", align='center')

    body_txt = urwid.Text(u"Body", align='center')
    body = urwid.Filler(body_txt, valign='middle')

    frame = urwid.Frame(body, header=header, footer=footer.render(), focus_part='body')

    loop = urwid.MainLoop(frame, unhandled_input=globle_input_listener)
    loop.run()

def globle_input_listener(key):
    footer.input_response(key)
