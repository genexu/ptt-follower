import urwid

test_list = ['test_post_0','test_post_1', 'test_post_2']

class FollowIdPostList(object):
    """Docstring For FollowIdPostList."""
    def __init__(self):
        super(FollowIdPostList, self).__init__()

    def render(self):
        post_list_item = [urwid.Text('Follow Id Post List'), urwid.Divider()]
        for post in test_list:
            button = urwid.Button(post)
            post_list_item.append(button)

        return urwid.ListBox(urwid.SimpleFocusListWalker(post_list_item))
