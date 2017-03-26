import urwid
import json
from header import Header
from body import Body
from footer import Footer

NORMAL = 'NORMAL'
ADD_NEW_ID = 'ADD_NEW_ID'
ADD_NEW_BOARD = 'ADD_NEW_BOARD'

class Bundle(object):
    """docstring for Bundle."""
    def __init__(self):
        super(Bundle, self).__init__()
        self.header = Header()
        self.body = Body()
        self.footer = Footer()
        self.status = NORMAL
        self.output = urwid.Frame(self.body.output, header=self.header.output, footer=self.footer.output, focus_part='body')

    def save_id(self, board_index, id):
        data = self.read_json_data()
        data['follow'][board_index]['id'].append(id)
        self.write_json_data(data)

    def save_board(self, board):
        board_data = {
            'board': board,
            'id': []
        }
        data = self.read_json_data()
        data['follow'].append(board_data)
        self.write_json_data(data)

    def read_json_data(self):
        with open('data.json', 'r') as data_file:
            return json.load(data_file)

    def write_json_data(self, data):
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file)

    def globle_input_listener(self, key):
        self.footer.input_response(key)
        if key in ('I'):
            self.status = ADD_NEW_ID
            self.footer.add_new_id()
            self.output.focus_position = 'footer'

        if key in ('B'):
            self.status = ADD_NEW_BOARD
            self.footer.add_new_board()
            self.output.focus_position = 'footer'

        if key in ('esc'):
            if self.status in (ADD_NEW_ID, ADD_NEW_BOARD):
                self.status = NORMAL
                self.footer.desc()
                self.output.focus_position = 'body'

        if key in ('enter'):
            if self.status in (ADD_NEW_ID):
                board_index = self.body.follow_id_list.board_index
                new_id = self.footer.output.focus.edit_text
                self.save_id(board_index, new_id)
                self.body.add_new_id(new_id)

            if self.status in (ADD_NEW_BOARD):
                new_board = self.footer.output.focus.edit_text
                self.save_board(new_board)
                self.body.add_new_board(new_board)

            if self.status in (ADD_NEW_ID, ADD_NEW_BOARD):
                self.status = NORMAL
                self.footer.desc()
                self.output.focus_position = 'body'

        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
