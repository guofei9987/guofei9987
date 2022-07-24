from bs4 import BeautifulSoup
import requests
import re
import sys


# %%
# https://github.com/egrcc/zhihu-python

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    'Host': "www.zhihu.com",
    'Origin': "http://www.zhihu.com",
    'Pragma': "no-cache",
    'Referer': "http://www.zhihu.com/"
}

url = 'https://www.zhihu.com/people/guo-fei-16-12'

r = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(r.content, "lxml")

# %%
stars = soup.find_all(name='div', attrs={'class': 'css-vurnku'})
print(stars[1].text)  # 点赞、喜欢、收藏

follows = soup.find_all(name='strong', attrs={'class': 'NumberBoard-itemValue'})
print(follows[1].text)  # 关注

# %%


agree, like, collection = re.findall('[0-9,]+', stars[1].text)

zhihu1 = '获得{}次赞同，{}次收藏，{}个关注'.format(agree, collection, follows[1].text)
zhihu2 = '获得{}次赞同/{}次喜欢/ {}次收藏/ {}个关注'.format(agree, like, collection, follows[1].text)

print(zhihu2)

with open('zhihu.svg', 'w') as svg:
    svg.write(f'''<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="510" height="20" role="img">
  <text x="0" y="15" >知乎{zhihu1}
  </text>
</svg>''')
