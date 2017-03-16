import urwid

test_list = ['test_board_0','test_board_1', 'test_board_2']

class FollowIdBoardList(object):
    """Docstring For FollowIdBoardList."""
    def __init__(self):
        super(FollowIdBoardList, self).__init__()

    def render(self):
        board_list_item = [urwid.Text('Follow Id Board List'), urwid.Divider()]
        for board in test_list:
            button = urwid.Button(board)
            board_list_item.append(button)

        return urwid.ListBox(urwid.SimpleFocusListWalker(board_list_item))
