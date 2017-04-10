import urwid
import json
import requests
import datetime
from bs4 import BeautifulSoup
from crawler import Crawler


STATUS = {
    'Standby': 'Standby',
    'WaitingForCrawling': 'WaitingForCrawling',
    'WaitingForRender': 'WaitingForRender'
}

class PostList(object):
    """Docstring For PostList."""
    def __init__(self, id_index = 0, board_index = 0, board = 'Test', ids = [], posts = [], crawl_number_of_page = 10):
        super(PostList, self).__init__()
        self.id_index = id_index
        self.board_index = board_index
        self.ids = ids
        self.board = board
        self.posts = posts
        self.crawl_number_of_page = crawl_number_of_page
        self.status = STATUS['Standby']

        self.update_config()

        bigtext = urwid.BigText('PTT FOLLOWER', urwid.Thin6x6Font())
        bigtext = urwid.Padding(bigtext, 'center', None)
        welcome_info = urwid.Text('Welcome, PTTer\nSelect The Board Or Press (R) To Load Post List', align='center')

        self.list_walker = urwid.SimpleFocusListWalker([bigtext, welcome_info])
        self.output = urwid.ListBox(self.list_walker)

    def update_id_index(self, index):
        self.id_index = index

    def update_board_index(self, index):
        self.board_index = index
        self.update_config()

    def update_config(self):
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)
            self.board = data_loaded['follow'][self.board_index]['board']
            self.ids = data_loaded['follow'][self.board_index]['id']
            self.crawl_number_of_page = data_loaded['settings']['crawl_number_of_page']

    def update_posts(self):
        self.update_config()
        del self.list_walker[:]
        self.list_walker.append(urwid.Text('Posts Updating...'))
        self.status = STATUS['WaitingForCrawling']


    def crawl_posts(self):
        crawler = Crawler(board = self.board, ids = self.ids)
        self.posts = crawler.request()

        for page in range(self.crawl_number_of_page - 1):
            crawler.url = crawler.domain + crawler.previous_page
            previous_page_post = crawler.request()
            for index in range(len(self.posts)):
                self.posts[index].extend(previous_page_post[index])
        self.status = STATUS['WaitingForRender']

    def render(self):
        self.update_config()

        post_list = []
        if len(self.posts) > 0:
            for post in self.posts[self.id_index]:
                post_datetime = datetime.datetime.fromtimestamp(int(post.timesteap)).strftime('%Y-%m-%d %H:%M:%S')
                button = urwid.Button('%s %s' %(post_datetime, post.title))
                post_list.append(button)

        del self.list_walker[:]
        for item in post_list:
            self.list_walker.append(item)
        self.status = STATUS['Standby']
