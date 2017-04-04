import urwid
import json
import requests
from bs4 import BeautifulSoup
from crawler import Crawler

class PostList(object):
    """Docstring For PostList."""
    def __init__(self, id_index = 0, board_index = 0, board = 'Test', ids = [], posts = []):
        super(PostList, self).__init__()
        self.id_index = id_index
        self.board_index = board_index
        self.ids = ids
        self.board = board
        self.posts = posts

        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][0]['board']
            self.ids = data_loaded['follow'][0]['id']

        self.update_posts()

        post_list = []
        for post in self.posts[self.id_index]:
            button = urwid.Button(post.title)
            post_list.append(button)

        self.list_walker = urwid.SimpleFocusListWalker(post_list)
        self.output = urwid.ListBox(self.list_walker)

    def update_id_index(self, index):
        self.id_index = index

    def update_board_index(self, index):
        self.board_index = index
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][self.board_index]['board']
            self.ids = data_loaded['follow'][self.board_index]['id']

    def update_posts(self):
        crawler = Crawler(board = self.board, ids = self.ids)
        self.posts = crawler.request()

    def render(self):
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][0]['board']
            self.id = data_loaded['follow'][0]['id']

        post_list = []
        for post in self.posts[self.id_index]:
            button = urwid.Button(post.title)
            post_list.append(button)

        del self.list_walker[:]
        for item in post_list:
            self.list_walker.append(item)
