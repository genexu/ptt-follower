import urwid
import json
import requests
from bs4 import BeautifulSoup
from crawler import Crawler

class PostList(object):
    """Docstring For PostList."""
    def __init__(self, index = 0, board = 'Test', ids = []):
        super(PostList, self).__init__()
        self.index = index
        self.ids = ids
        self.board = board

        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][0]['board']
            self.ids = data_loaded['follow'][0]['id']

        crawler = Crawler(board = self.board, ids = self.ids)
        posts = crawler.request()

        post_list = []
        for post in posts[self.index]:
            button = urwid.Button(post.title)
            post_list.append(button)

        post_list.insert(0, urwid.Divider())
        post_list.insert(0, urwid.Text('POST'))

        self.list_walker = urwid.SimpleFocusListWalker(post_list)
        self.output = urwid.ListBox(self.list_walker)

    def update_id_index(self, index):
        self.index = index

    def render(self):
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][0]['board']
            self.id = data_loaded['follow'][0]['id']

        crawler = Crawler(board = self.board, ids = self.ids)
        posts = crawler.request()

        post_list = []
        for post in posts[self.index]:
            button = urwid.Button(post.title)
            post_list.append(button)

        post_list.insert(0, urwid.Divider())
        post_list.insert(0, urwid.Text('POST'))

        del self.list_walker[:]
        for item in post_list:
            self.list_walker.append(item)
