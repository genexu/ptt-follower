import urwid
import json
from header import Header
from body import Body
from footer import Footer

NORMAL = 'NORMAL'
ADD_NEW_ID = 'ADD_NEW_ID'
ADD_NEW_BOARD = 'ADD_NEW_BOARD'
DELETE_ID = 'DELETE_ID'
DELETE_BOARD = 'DELETE_BOARD'

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

    def delete_id(self, board_index, id_index):
        data = self.read_json_data()
        data['follow'][board_index]['id'].pop(id_index)
        self.write_json_data(data)

    def delete_board(self, board_index):
        data = self.read_json_data()
        data['follow'].pop(board_index)
        self.write_json_data(data)

    def read_json_data(self):
        with open('data.json', 'r') as data_file:
            return json.load(data_file)

    def write_json_data(self, data):
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file)

    def globle_input_listener(self, key):
        self.footer.input_response(repr(key))
        if repr(key) in ("'I'"):
            self.status = ADD_NEW_ID
            self.footer.add_new_id()
            self.output.focus_position = 'footer'

        if repr(key) in ("'B'"):
            self.status = ADD_NEW_BOARD
            self.footer.add_new_board()
            self.output.focus_position = 'footer'

        if repr(key) in ("'D'"):
            BOARD_LIST_INDEX = 0
            ID_LIST_INDEX = 1
            
            body_content_focus_postion = self.body.content.focus_position
            if body_content_focus_postion in (BOARD_LIST_INDEX, ID_LIST_INDEX):
                delete_item = self.body.content.focus
                delete_item_position = delete_item.focus_position

                if body_content_focus_postion == BOARD_LIST_INDEX:
                    self.status = DELETE_BOARD
                    self.footer.delete_board(delete_item_position)
                if body_content_focus_postion == ID_LIST_INDEX:
                    self.status = DELETE_ID
                    self.footer.delete_id(delete_item_position)

                self.output.focus_position = 'footer'

        if repr(key) in ("'R'"):
            self.body.post_list.update_posts()

        if repr(key) in ("'esc'"):
            if self.status in (ADD_NEW_ID, ADD_NEW_BOARD, DELETE_ID, DELETE_BOARD):
                self.status = NORMAL
                self.footer.desc()
                self.output.focus_position = 'body'

        if repr(key) in ("'enter'"):
            if self.status in (ADD_NEW_ID):
                board_index = self.body.id_list.board_index
                new_id = self.footer.output.focus.edit_text
                self.save_id(board_index, new_id)
                self.body.add_new_id(new_id)

            if self.status in (ADD_NEW_BOARD):
                new_board = self.footer.output.focus.edit_text
                self.save_board(new_board)
                self.body.add_new_board(new_board)

            if self.status in (DELETE_ID):
                ans = self.footer.output.focus.edit_text
                if ans == 'y':
                    body_content_focus = self.body.content.focus
                    delete_item = self.body.content.focus
                    delete_item_position = delete_item.focus_position
                    board_index = self.body.id_list.board_index
                    self.delete_id(board_index, delete_item_position)
                    self.body.delete_id(delete_item_position)

            if self.status in (DELETE_BOARD):
                ans = self.footer.output.focus.edit_text
                if ans == 'y':
                    body_content_focus = self.body.content.focus
                    delete_item = self.body.content.focus
                    delete_item_position = delete_item.focus_position
                    self.delete_board(delete_item_position)
                    self.body.delete_board(delete_item_position)

            if self.status in (ADD_NEW_ID, ADD_NEW_BOARD, DELETE_ID, DELETE_BOARD):
                self.status = NORMAL
                self.footer.desc()
                self.output.focus_position = 'body'

        if repr(key) in ("'q'", "'Q'"):
            raise urwid.ExitMainLoop()
