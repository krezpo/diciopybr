import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class Termos:

    def __init__(self):
        self.url_sinonimos = "https://sinonimos.com.br/"

    def get_sinonimos(self, termo):
        url       = self.url_sinonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        sinonimos = []

        for div in soup.find_all('a'):
            div   = str(div).replace("</a>", "")
            start = div.find(">") + 1
            sinonimos.append(div[start:])

        for div in soup.find_all('span'):
            sinonimos.append(str(div).replace("<span>", "").replace("</span>", ""))

        return sinonimos

    def get_antonimos(self, termo):

        pass