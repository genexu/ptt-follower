import urwid

def run():
    header = urwid.Text(u"Header", align='center')

    body_txt = urwid.Text(u"Body", align='center')
    body = urwid.Filler(body_txt, valign='middle')

    footer = urwid.Text(u"Footer", align='center')

    frame = urwid.Frame(body, header=header, footer=footer, focus_part='body')

    loop = urwid.MainLoop(frame)
    loop.run()
