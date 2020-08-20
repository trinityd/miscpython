from bs4 import BeautifulSoup as BS
import requests

r = requests.get('https://www.nytimes.com')
soup = BS(r.text, 'html.parser')

for article in soup.find_all('article'):
    print(article.h2.string)