import urwid
import json

class FollowIdBoardList(object):
    """Docstring For FollowIdBoardList."""
    def __init__(self, id_index = 0, list_item = []):
        super(FollowIdBoardList, self).__init__()
        self.id_index = id_index
        self.list_item = list_item

    def update_id_index(self, index):
        self.id_index = index

    def render(self):
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.list_item = data_loaded['follow'][self.id_index]['board']

        board_list_item = [urwid.Text('Follow Id Board List'), urwid.Divider()]
        for board in self.list_item:
            button = urwid.Button(board)
            board_list_item.append(button)

        return urwid.ListBox(urwid.SimpleFocusListWalker(board_list_item))
