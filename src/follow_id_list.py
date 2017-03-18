import urwid
import json

class FollowIdList(object):
    """Docstring For Follow_Id_List."""
    def __init__(self, list_item = []):
        super(FollowIdList, self).__init__()
        self.list_item = list_item

    def render(self):
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            for f in data_loaded['follow']:
                self.list_item.append(f['id'])

        id_list_item = [urwid.Text('Follow Id List'), urwid.Divider()]
        for user_id in self.list_item:
            button = urwid.Button(user_id)
            id_list_item.append(button)

        return urwid.ListBox(urwid.SimpleFocusListWalker(id_list_item))
