import urwid
import json

class BoardList(object):
    """Docstring For BoardList."""
    def __init__(self, change_focus_board):
        super(BoardList, self).__init__()
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

        self.change_focus_board = change_focus_board
        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def on_board_clicked(self, button):
        board_position = self.output.focus_position
        self.change_focus_board(board_position)

    def add(self, board):
        button = urwid.Button(board)
        urwid.connect_signal(button, 'click', self.on_board_clicked)
        self.list_walker.append(button)

    def delete(self, board_index):
        self.list_walker.pop(board_index)
