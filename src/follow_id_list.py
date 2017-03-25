import urwid
import json

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self, board_index = 0):
        super(FollowIdList, self).__init__()
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for user_id in data_loaded['follow'][board_index]['id']:
                button = urwid.Button(user_id)
                list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))

        self.board_index = board_index
        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def update_board_index(self, index):
        self.board_index = index

    def add(self, id):
        button = urwid.Button(id)
        self.list_walker.append(button)

    def render(self):
        json_data_list = []
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            json_data_list = data_loaded['follow'][self.board_index]['id']

        for id in json_data_list:
            button = urwid.Button(id)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))

        del self.list_walker[:]
        for item in list_item:
            self.list_walker.append(item)
