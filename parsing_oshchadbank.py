import urllib.request
from bs4 import BeautifulSoup

class ParsingOshchadbank:
    def __init__(self):
        self.base_url = 'http://www.oschadbank.ua/ua/'

    def get_html(self, url):
        response = urllib.request.urlopen(url)
        return response.read()

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('div', class_ = 'currency-wrap')
        cour = []
        for i in table.find_all('strong'):
            cour.append(i.text)
        courses = []
        courses.append({'bank':'Ощадбанк', 'name': 'USD', 'case': cour[0], 'sale': cour[1]})
        courses.append({'bank':'Ощадбанк', 'name': 'EUR', 'case': cour[2], 'sale': cour[3]})
        courses.append({'bank':'Ощадбанк', 'name': 'RUR', 'case': cour[4], 'sale': cour[5]})

        return courses

    def get_value(self):
        return self.parse(self.get_html(self.base_url))
