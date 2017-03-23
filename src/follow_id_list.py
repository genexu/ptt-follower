import urwid
import json

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self):
        super(FollowIdList, self).__init__()
        json_data_list = []
        list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for f in data_loaded['follow']:
                json_data_list.append(f['id'])

        for user_id in json_data_list:
            button = urwid.Button(user_id)
            list_item.append(button)

        list_item.insert(0, urwid.Divider())
        list_item.insert(0, urwid.Text('ID'))

        self.list_walker = urwid.SimpleFocusListWalker(list_item)
        self.output = urwid.ListBox(self.list_walker)

    def add(self, id):
        self.list_walker.append(urwid.Button(id))

    def render(self):
        return self.output
