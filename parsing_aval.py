import urllib.request
from bs4 import BeautifulSoup

class ParsingAval:
    def __init__(self):
        self.base_url = 'https://www.aval.ua/personal/everyday/exchange/exchange/'    

    def get_html(self, url):
        response = urllib.request.urlopen(url)
        return response.read()

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')


        sk = soup.find_all('div', class_ = 'body-currency')
        table = soup.find_all('td', class_ = 'right')

        cour = []
        for i in table[:6]:
            cour.append(i.text)
        courses = []
        courses.append({'bank': 'Банк Аваль', 'name': 'USD', 'case': cour[0], 'sale': cour[1]})
        courses.append({'bank': 'Банк Аваль', 'name': 'EUR', 'case': cour[2], 'sale': cour[3]})
        courses.append({'bank': 'Банк Аваль', 'name': 'RUR', 'case': cour[4], 'sale': cour[5]})

        return courses
    
    def get_value(self):
         return self.parse(self.get_html(self.base_url))

