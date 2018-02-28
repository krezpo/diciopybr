import requests
from bs4 import BeautifulSoup

class Termos:

    def __init__(self):
        self.url_sinonimos = "https://sinonimos.com.br/"

    def get_sinonimos(self, termo):
        url       = self.url_sinonimos + "{}/".format(termo)
        html      = requests.get(url).text
        soup      = BeautifulSoup(html, 'html.parser')
        sinonimos = []

        for div in soup.find_all('a'):
            if div.get('class') == ['sinonimo']:
                d     = str(div)
                start = d.find(">") + 1
                sinonimos.append(d[start:].replace("</a>", ""))

        return sinonimos
