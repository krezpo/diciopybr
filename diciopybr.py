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

        :param termo:string
        :return sinonimos:list
        '''
        url       = self.url_sinonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        sinonimos = []

        for div in soup.find_all('a'):
            sinonimos.append(div.get_text())

        for div in soup.find_all('span'):
            sinonimos.append(div.get_text())

        return sinonimos

    def get_antonimos(self, termo):
        '''
        Retorna a lista de antonimos de um dado termo.

        :param termo:string
        :return antonimos:list
        '''
        url       = self.url_antonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        soup      = BeautifulSoup(str(soup.select('div.s-wrapper')), 'html.parser')
        antonimos = []

        for div in soup.find_all('a'):
            antonimos.append(div.get_text())

        return antonimos

    def get_sentidos(self, termo):
        '''
        Retorna a lista de sentidos de um determinado termo.

        :param termo:string
        :return sentidos:list
        '''
        url      = self.url_sinonimos + "{}/".format(termo)
        html     = requests.get(url).text
        soup     = BeautifulSoup(html, 'html.parser')
        soup     = BeautifulSoup(str(soup.select('div.sentido')), 'html.parser')
        sentidos = []

        for s in soup:
            if isinstance(s, Tag):
                sentidos.append(s.get_text()[:-1])

        return sentidos