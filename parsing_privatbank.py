import urllib.request
from bs4 import BeautifulSoup

class ParsingPrivatbank:
    def __init__(self):
        self.base_url = 'https://privatbank.ua/'

    def get_html(self, url):
        response = urllib.request.urlopen(url)
        return response.read()

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('tbody', id='selectByPB')
        cour = []
        for row in table.find_all('td', style="text-align:right;"):
            cour.append(row.text)
        courses = []
        courses.append({'bank':'Приватбанк', 'name': 'USD', 'case': cour[2], 'sale': cour[3]})
        courses.append({'bank':'Приватбанк', 'name': 'EUR', 'case': cour[0], 'sale': cour[1]})
        courses.append({'bank':'Приватбанк', 'name': 'RUR', 'case': cour[4], 'sale': cour[5]})

        return courses

    def get_value(self):
        return self.parse(self.get_html(self.base_url))
    
