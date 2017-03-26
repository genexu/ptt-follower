import urwid

class FollowIdPostList(object):
    """Docstring For FollowIdPostList."""
    def __init__(self):
        super(FollowIdPostList, self).__init__()
        post_list_item = [urwid.Text('Post'), urwid.Divider()]
        self.output = urwid.ListBox(urwid.SimpleFocusListWalker(post_list_item))
