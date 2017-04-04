import urwid
import json

class IdList(object):
    """Docstring For id_list."""
    def __init__(self, change_focus_id):
        super(IdList, self).__init__()
        self.change_focus_id = change_focus_id
        self.board_index = 0
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for user_id in data_loaded['follow'][self.board_index]['id']:
                button = urwid.Button(user_id)
                urwid.connect_signal(button, 'click', self.on_id_clicked)
                list_item.append(button)

        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def update_board_index(self, index):
        self.board_index = index

    def on_id_clicked(self, button):
        id_position = self.output.focus_position
        self.change_focus_id(id_position)

    def add(self, id):
        button = urwid.Button(id)
        urwid.connect_signal(button, 'click', self.on_id_clicked)
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

        del self.list_walker[:]
        for item in list_item:
            self.list_walker.append(item)
