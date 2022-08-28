import requests

about_url = 'https://raw.githubusercontent.com/guofei9987/guofei9987.github.io/master/pages/about.md'

r = requests.get(about_url)

content = r.content.decode('utf-8').replace('''---
layout: page
title: 关于
---

''', '')

with open('README.md', 'w') as f:
    f.write(content)
