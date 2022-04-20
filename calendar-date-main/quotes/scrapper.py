"""

"""
import json
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    quotes = []
    url = 'https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%85%D8%AB%D8%A7%D9%84_%D9%85%D8%B5%D8%B1%D9%8A%D8%A9'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    ul = soup.find_all('ul')[0]
    for li in ul.find_all('li'):
        try:
            quotes.append(li.find('b').text)
        except AttributeError as e:
            print(e)

    with open('wiki_quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)


