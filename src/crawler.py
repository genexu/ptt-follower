import requests
from bs4 import BeautifulSoup
from post import Post

class Crawler(object):
    """Docstring For Crawler."""
    def __init__(self, domain = 'https://www.ptt.cc/bbs/', board = 'Test', ids=[]):
        super(Crawler, self).__init__()
        self.domain = domain
        self.board = board
        self.ids = ids
        self.url = self.domain + self.board + '/index.html'
        self.next_page = ''
        self.previous = ''

    def request(self):
        r = requests.get(self.url)

        if r.status_code != requests.codes.ok:
            return []

        results = [[] for _ in range(len(self.ids))]

        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.find_all('div', class_="r-ent")

        for post in posts:
            title = post.find('div', class_="title").get_text().strip()
            meta = post.find('div', class_='meta')
            date = post.find('div', class_='date').get_text()
            author = meta.find('div', class_='author').get_text()

            if author != '-' and author in self.ids:
                results[self.ids.index(author)].append(Post(title = title, author = author, date = date))

        return results
