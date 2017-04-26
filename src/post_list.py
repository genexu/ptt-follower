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
        self.crawler = Crawler(board = self.board, ids = self.ids)
        self.crawl_number_of_page = crawl_number_of_page
        self.crawl_number_now = 0
        self.status = STATUS['Standby']


        self.update_config()

        welcome_info = urwid.Text('Welcome, PTTer\nSelect The Board Or Press (R) To Load Post List', align='center')

        self.list_walker = urwid.SimpleFocusListWalker([welcome_info])
        self.output = urwid.ListBox(self.list_walker)

    def update_id_index(self, index):
        self.id_index = index

    def update_board_index(self, index):
        self.board_index = index
        self.update_config()

    def update_crawl_number_of_page(self, n):
        self.crawl_number_of_page = n

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
        self.crawler.board = self.board
        self.crawler.ids = self.ids
        self.crawler.init_url()

        del self.list_walker[:]
        self.list_walker.append(urwid.Text('Posts Updating...(%s/%s)' % (self.crawl_number_now, self.crawl_number_of_page)))

        if self.crawl_number_now == 0:
            self.posts = self.crawler.request()
        else:
            self.crawler.url = self.crawler.domain + self.crawler.previous_page
            previous_page_post = self.crawler.request()
            for index in range(len(self.posts)):
                self.posts[index].extend(previous_page_post[index])

        self.crawl_number_now += 1

        if self.crawler.previous_page == False or self.crawl_number_now > self.crawl_number_of_page:
            self.crawl_number_now = 0
            self.status = STATUS['WaitingForRender']
            return

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
