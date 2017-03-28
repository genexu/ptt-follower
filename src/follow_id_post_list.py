import urwid
import json
import requests
from bs4 import BeautifulSoup

class FollowIdPostList(object):
    """Docstring For FollowIdPostList."""
    def __init__(self):
        super(FollowIdPostList, self).__init__()
        board = ''
        id = []
        post_list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            board = data_loaded['follow'][0]['board']
            id = data_loaded['follow'][0]['id']
            num_of_tracking_page  = 10

        post_list = [[]] * len(id)

        domain = 'https://www.ptt.cc/bbs/'
        url = domain + board + '/index.html'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.find_all('div', class_="r-ent")

        for post in posts:
            title = post.find('div', class_="title").get_text().strip()
            meta = post.find('div', class_='meta')
            author = meta.find('div', class_='author').get_text()

            if author != '-' and author in id:
                post_list[id.index(author)].append(title)

        for post in post_list[0]:
            button = urwid.Button(post)
            post_list_item.append(button)

        post_list_item.insert(0, urwid.Divider())
        post_list_item.insert(0, urwid.Text('POST'))

        self.list_walker = urwid.SimpleFocusListWalker(post_list_item)
        self.output = urwid.ListBox(self.list_walker)
