import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class Termos:

    def __init__(self):
        self.url_sinonimos = "https://sinonimos.com.br/"
        self.url_antonimos = "https://antonimos.com.br/"

    def get_sinonimos(self, termo):
        url       = self.url_sinonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        sinonimos = []

        for div in soup.find_all('a'):
            d     = str(div).replace("</a>", "")
            start = d.find(">") + 1
            sinonimos.append(d[start:])

        for div in soup.find_all('span'):
            sinonimos.append(str(div).replace("<span>", "").replace("</span>", ""))

        return sinonimos

    def get_antonimos(self, termo):
        url       = self.url_antonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        antonimos = []

        for div in soup.find_all('a'):
            d = str(div).replace("</a>", "")
            start = d.find(">") + 1
            antonimos.append(d[start:])

        return antonimos

    def get_sentidos(self, termo):

        pass