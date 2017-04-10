import requests
from bs4 import BeautifulSoup
from post import Post
import re
from pprint import pprint

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
            meta = post.find('div', class_='meta')
            author = meta.find('div', class_='author').get_text()

            if author != '-' and author in self.ids:
                title_with_link = post.find('div', class_="title")
                title = title_with_link.get_text().strip()
                url = 'None'
                if title_with_link.a != None:
                    url = self.domain + title_with_link.a.get('href')
                date = post.find('div', class_='date').get_text()
                regex = r"M\.(.*)\.A"
                timesteap = re.search(regex, url).group(1)
                results[self.ids.index(author)].append(Post(title = title, author = author, date = date, url = url, timesteap = timesteap))

        return results
