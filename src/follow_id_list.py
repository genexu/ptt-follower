import urwid
import json

TITLE_AND_DIV_ROW = 2

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self, change_focus_id):
        super(FollowIdList, self).__init__()
        json_data_list = []
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for f in data_loaded['follow']:
                json_data_list.append(f['id'])

        for user_id in json_data_list:
            button = urwid.Button(user_id)
            urwid.connect_signal(button, 'click', self.on_id_clicked)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))

        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)
        self.change_focus_id = change_focus_id

    def on_id_clicked(self, button):
        id_position = self.output.focus_position
        self.change_focus_id(id_position - TITLE_AND_DIV_ROW)

    def add(self, id):
        button = urwid.Button(id)
        urwid.connect_signal(button, 'click', self.on_id_clicked)
        self.list_walker.append(button)

    def render(self):
        return self.output
