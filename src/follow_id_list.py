import urwid

test_list = ['test_follow_id_0','test_follow_id_1', 'test_follow_id_2']

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self):
        super(FollowIdList, self).__init__()

    def render(self):
        id_list_item = [urwid.Text('Follow Id List'), urwid.Divider()]
        for user_id in test_list:
            button = urwid.Button(user_id)
            id_list_item.append(button)

        return urwid.ListBox(urwid.SimpleFocusListWalker(id_list_item))
