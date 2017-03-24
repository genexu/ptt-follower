import urwid
import json

class FollowIdBoardList(object):
    """Docstring For FollowIdBoardList."""
    def __init__(self, id_index = 0, list_item = []):
        super(FollowIdBoardList, self).__init__()
        self.id_index = id_index
        self.list_walker = urwid.SimpleFocusListWalker(self.gen_list())
        self.output = urwid.ListBox(self.list_walker)

    def change_follow_id(self):
        list_item = self.gen_list()
        del self.list_walker[:]
        for item in list_item:
            self.list_walker.append(item)

    def gen_list(self):
        json_data_list = []
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            json_data_list = data_loaded['follow'][self.id_index]['board']

        for board in json_data_list:
            button = urwid.Button(board)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('BOARD'))

        return list_item

    def update_id_index(self, index):
        self.id_index = index

    def add(self, board):
        button = urwid.Button(board)
        self.list_walker.append(button)

    def render(self):
        return self.output
