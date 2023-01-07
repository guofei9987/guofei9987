import requests
from bs4 import BeautifulSoup

about_url = 'https://www.guofei.site/pages/about.html'

r = requests.get(about_url)
soup = BeautifulSoup(r.text, 'lxml')

about = soup.find(name='div', attrs={"id": "page-content"})
with open('README2.md', 'w') as f:
    f.write(about.decode_contents())
