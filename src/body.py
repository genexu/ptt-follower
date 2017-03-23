import urwid
from follow_id_list import FollowIdList
from follow_id_board_list import FollowIdBoardList
from follow_id_post_list import FollowIdPostList

WEIGHT = 'weight'
SIDEBAR_WEIGHT = 0.3

class Body(object):
    """Docstring For Body."""
    def __init__(self):
        super(Body, self).__init__()
        self.follow_id_list = FollowIdList(change_focus_id = self.on_change_focus_id)
        self.follow_id_board_list = FollowIdBoardList()
        self.follow_id_post_list = FollowIdPostList()

    def on_change_focus_id(self, id):
        self.follow_id_board_list.update_id_index(id)
        self.follow_id_board_list.change_follow_id()

    def add_new_id(self, id):
        self.follow_id_list.add(id)

    def render(self):
        return urwid.Columns([(WEIGHT, SIDEBAR_WEIGHT, self.follow_id_list.render()), (WEIGHT, SIDEBAR_WEIGHT, self.follow_id_board_list.render()), self.follow_id_post_list.render()])
