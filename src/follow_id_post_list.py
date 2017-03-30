import urwid
import json
import requests
from bs4 import BeautifulSoup

class FollowIdPostList(object):
    """Docstring For FollowIdPostList."""
    def __init__(self, index = 0):
        super(FollowIdPostList, self).__init__()
        self.index = index
        board = ''
        id = []
        post_list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            board = data_loaded['follow'][0]['board']
            id = data_loaded['follow'][0]['id']

        post_list = arr = [[] for _ in range(len(id))]

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
                post_list[id.index(author)].append(author + title)

        for post in post_list[self.index]:
            button = urwid.Button(post)
            post_list_item.append(button)

        post_list_item.insert(0, urwid.Divider())
        post_list_item.insert(0, urwid.Text('POST'))

        self.list_walker = urwid.SimpleFocusListWalker(post_list_item)
        self.output = urwid.ListBox(self.list_walker)

    def update_id_index(self, index):
        self.index = index

    def render(self):
        id = []
        post_list_item = []
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            board = data_loaded['follow'][0]['board']
            id = data_loaded['follow'][0]['id']

        post_list = arr = [[] for _ in range(len(id))]

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
                post_list[id.index(author)].append(author + title)

        for post in post_list[self.index]:
            button = urwid.Button(post)
            post_list_item.append(button)

        post_list_item.insert(0, urwid.Divider())
        post_list_item.insert(0, urwid.Text('POST'))

        del self.list_walker[:]
        for item in post_list_item:
            self.list_walker.append(item)
