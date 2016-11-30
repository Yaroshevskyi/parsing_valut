import urllib.request
from bs4 import BeautifulSoup

class ParsingPumbBank:
    def __init__(self):
        self.base_url = 'http://pumb.ua/ru/'

    def get_html(self, url):
        response = urllib.request.urlopen(url)
        return response.read()

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        sk = soup.find_all('div', class_= 'tabs-conteiner')
        table = soup.find_all('strong')
        cour = []
        for i in table[:6]:
            cour.append(i.text)
        courses = []
        courses.append({'bank': 'ПУМБ Банк', 'name': 'USD', 'case': cour[0], 'sale': cour[1]})
        courses.append({'bank': 'ПУМБ Банк', 'name': 'EUR', 'case': cour[4], 'sale': cour[5]})
        courses.append({'bank': 'ПУМБ Банк', 'name': 'RUR', 'case': cour[2], 'sale': cour[3]})

        return courses

    def get_value(self):
        return self.parse(self.get_html(self.base_url))
