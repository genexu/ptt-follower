import urwid
from id_list import IdList
from board_list import BoardList
from post_list import PostList

WEIGHT = 'weight'
SIDEBAR_WEIGHT = 0.3

class Body(object):
    """Docstring For Body."""
    def __init__(self):
        super(Body, self).__init__()
        self.board_list = BoardList(change_focus_board = self.on_change_focus_board)
        self.id_list = IdList(change_focus_id = self.on_change_focus_id)
        self.post_list = PostList()
        self.output = urwid.Columns([(WEIGHT, SIDEBAR_WEIGHT, self.board_list.output), (WEIGHT, SIDEBAR_WEIGHT, self.id_list.output), self.post_list.output])

    def on_change_focus_board(self, id):
        self.id_list.update_board_index(id)
        self.id_list.render()

    def on_change_focus_id(self, index):
        self.post_list.update_id_index(index)
        self.post_list.render()

    def add_new_id(self, id):
        self.id_list.add(id)

    def add_new_board(self, board):
        self.board_list.add(board)
