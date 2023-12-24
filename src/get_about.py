import requests
from bs4 import BeautifulSoup

about_url = 'https://www.guofei.site/me.html'

r = requests.get(about_url)
soup = BeautifulSoup(r.text, 'lxml')

about = soup.find(name='div', attrs={"id": "page-content"})
# img 链接无法生效。但 object 在 github 首页不显示
with open('README.md', 'w') as f:
    f.write(about.decode_contents().
            replace('''<object data="https://www.guofei.site/pages/trophy.svg"></object>''',
                    '''<img src="https://www.guofei.site/pages/trophy.svg">''')
            .replace(
        '''<span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa  fa-stack-1x fa-inverse">知</i></span>''',
        '')
            )
