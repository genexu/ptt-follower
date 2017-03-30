import urwid
import json

TITLE_AND_DIV_ROW = 2

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self, change_focus_id):
        super(FollowIdList, self).__init__()
        self.change_focus_id = change_focus_id
        self.board_index = 0
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for user_id in data_loaded['follow'][self.board_index]['id']:
                button = urwid.Button(user_id)
                urwid.connect_signal(button, 'click', self.on_id_clicked)
                list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))


        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def update_board_index(self, index):
        self.board_index = index

    def on_id_clicked(self, button):
        id_position = self.output.focus_position
        self.change_focus_id(id_position - TITLE_AND_DIV_ROW)

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
            urwid.connect_signal(button, 'click', self.on_id_clicked)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))

        del self.list_walker[:]
        for item in list_item:
            self.list_walker.append(item)
