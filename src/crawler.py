import requests
from bs4 import BeautifulSoup
from post import Post
import re

class Crawler(object):
    """Docstring For Crawler."""
    def __init__(self, domain = 'https://www.ptt.cc', board = 'Test', ids=[]):
        super(Crawler, self).__init__()
        self.domain = domain
        self.board = board
        self.ids = ids
        self.url = self.domain + '/bbs/' + self.board + '/index.html'
        self.next_page = False
        self.previous_page = False

    def init_url(self):
        self.url = self.domain + '/bbs/' + self.board + '/index.html'

    def request(self):
        r = requests.get(self.url)

        if r.status_code != requests.codes.ok:
            return []

        results = [[] for _ in range(len(self.ids))]

        soup = BeautifulSoup(r.text, 'html.parser')

        previous_page = soup.find('a', text = re.compile(unicode("上頁", "utf8")), attrs = {'class' : 'btn wide'})
        if previous_page:
            self.previous_page = previous_page.get('href')

        next_page = soup.find('a', text = re.compile(unicode("下頁", "utf8")), attrs = {'class' : 'btn wide'})
        if next_page:
            self.next_page = next_page.get('href')

        posts = soup.find_all('div', class_="r-ent")

        for post in posts:
            title = post.find('div', class_="title").get_text().strip()
            meta = post.find('div', class_='meta')
            date = post.find('div', class_='date').get_text()
            author = meta.find('div', class_='author').get_text()

            if author != '-' and author in self.ids:
                results[self.ids.index(author)].append(Post(title = title, author = author, date = date))

        return results
