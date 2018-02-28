import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class Termos:
    '''
    Coded by Eduardo Germano
    '''

    def __init__(self):
        self.url_sinonimos = "https://sinonimos.com.br/"
        self.url_antonimos = "https://antonimos.com.br/"

    def get_sinonimos(self, termo):
        '''
        Retorna a lista de sinonimos de um determinado termo.

        :param termo:
        :return list:sinonimos
        '''
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
        '''
        Retorna a lista de antonimos de um dado termo.

        :param termo:
        :return list:antonimos
        '''

        url       = self.url_antonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        antonimos = []

        for div in soup.find_all('a'):
            d     = str(div).replace("</a>", "")
            start = d.find(">") + 1
            antonimos.append(d[start:])

        return antonimos

    def get_sentidos(self, termo):
        '''
        Retorna a lista de sentidos de um determinado termo.

        :param termo:
        :return list:sentidos
        '''

        url      = self.url_sinonimos + "{}/".format(termo)
        html     = requests.get(url).text
        soup     = BeautifulSoup(html, 'html.parser')
        soup     = BeautifulSoup(str(soup.select('div.sentido')), 'html.parser')
        sentidos = []

        for s in soup:
            if isinstance(s, Tag):
                sentidos.append(str(s).replace('<div class="sentido">', "").replace(":</div>", ""))

        return sentidos