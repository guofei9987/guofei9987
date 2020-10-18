from bs4 import BeautifulSoup
import requests
import re
import sys

handle = sys.argv[1]
token = sys.argv[2]
readmePath = sys.argv[3]

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

zhihu = '获得{}次赞同，{}次喜欢，{}次收藏，{}个关注'.format(agree, like, collection, follows[1].text)

with open(readmePath, "r") as readme:
    content = readme.read()

newContent = re.sub(r"(?<=<!\-\-START_SECTION:zhihu\-followers\-\->)[\s\S]*(?=<!\-\-END_SECTION:zhihu\-followers\-\->)",
                    f"\n{zhihu}\n", content)

with open(readmePath, "w") as readme:
    readme.write(newContent)
