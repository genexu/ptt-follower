import urwid
import json

TITLE_AND_DIV_ROW = 2

class FollowIdBoardList(object):
    """Docstring For FollowIdBoardList."""
    def __init__(self, change_focus_board):
        super(FollowIdBoardList, self).__init__()
        json_data_list = []
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for f in data_loaded['follow']:
                json_data_list.append(f['board'])
        for board in json_data_list:
            button = urwid.Button(board)
            urwid.connect_signal(button, 'click', self.on_board_clicked)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('BOARD'))

        self.change_focus_board = change_focus_board
        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def on_board_clicked(self, button):
        board_position = self.output.focus_position
        self.change_focus_board(board_position - TITLE_AND_DIV_ROW)

    def add(self, board):
        button = urwid.Button(board)
        urwid.connect_signal(button, 'click', self.on_board_clicked)
        self.list_walker.append(button)
