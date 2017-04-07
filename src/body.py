import urwid
from id_list import IdList
from board_list import BoardList
from post_list import PostList

WEIGHT = 'weight'
SIDEBAR_WEIGHT = 0.3

POST_LIST_STATUS = {
    'Standby': 'Standby'
}

class Body(object):
    """Docstring For Body."""
    def __init__(self):
        super(Body, self).__init__()
        self.board_list = BoardList(change_focus_board = self.on_change_focus_board)
        self.id_list = IdList(change_focus_id = self.on_change_focus_id)
        self.post_list = PostList()
        self.title = urwid.Columns([(WEIGHT, SIDEBAR_WEIGHT, urwid.Text('BOARD')), (WEIGHT, SIDEBAR_WEIGHT, urwid.Text('ID')), urwid.Text('POST')])
        self.content = urwid.Columns([(WEIGHT, SIDEBAR_WEIGHT, self.board_list.output), (WEIGHT, SIDEBAR_WEIGHT, self.id_list.output), self.post_list.output])
        self.output = urwid.Frame(self.content, header = self.title)

    def on_change_focus_board(self, index):
        if self.post_list.status != POST_LIST_STATUS['Standby']:
            return
        self.id_list.update_board_index(index)
        self.id_list.render()
        self.post_list.update_id_index(0)
        self.post_list.update_board_index(index)
        self.post_list.update_posts()

    def on_change_focus_id(self, index):
        self.post_list.update_id_index(index)
        self.post_list.render()

    def add_new_id(self, id):
        self.id_list.add(id)
        self.post_list.update_posts()

    def add_new_board(self, board):
        self.board_list.add(board)

    def delete_id(self, id_index):
        self.id_list.delete(id_index)
        self.post_list.update_id_index(0)
        self.post_list.update_posts()

    def delete_board(self, board_index):
        self.board_list.delete(board_index)
        self.id_list.update_board_index(0)
        self.id_list.render()
        self.post_list.update_id_index(0)
        self.post_list.update_board_index(0)
        self.post_list.update_posts()
