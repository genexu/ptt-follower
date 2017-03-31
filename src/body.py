import urwid
from follow_id_list import FollowIdList
from board_list import BoardList
from follow_id_post_list import FollowIdPostList

WEIGHT = 'weight'
SIDEBAR_WEIGHT = 0.3

class Body(object):
    """Docstring For Body."""
    def __init__(self):
        super(Body, self).__init__()
        self.board_list = BoardList(change_focus_board = self.on_change_focus_board)
        self.follow_id_list = FollowIdList(change_focus_id = self.on_change_focus_id)
        self.follow_id_post_list = FollowIdPostList()
        self.output = urwid.Columns([(WEIGHT, SIDEBAR_WEIGHT, self.board_list.output), (WEIGHT, SIDEBAR_WEIGHT, self.follow_id_list.output), self.follow_id_post_list.output])

    def on_change_focus_board(self, id):
        self.follow_id_list.update_board_index(id)
        self.follow_id_list.render()

    def on_change_focus_id(self, index):
        self.follow_id_post_list.update_id_index(index)
        self.follow_id_post_list.render()

    def add_new_id(self, id):
        self.follow_id_list.add(id)

    def add_new_board(self, board):
        self.board_list.add(board)
