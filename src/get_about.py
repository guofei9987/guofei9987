import requests

about_url = 'https://raw.githubusercontent.com/guofei9987/guofei9987.github.io/master/pages/about.md'

resp = requests.get(about_url)

with open('about.md', 'wb') as f:
    f.write(resp.content)
