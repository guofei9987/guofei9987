import json
from bs4 import BeautifulSoup

with open('achievement.json', 'r') as f:
    achievement = json.load(f)

# %% 获取：读书xx本
import requests

r = requests.get('https://www.guofei.site/pages/book_list.json')
book_list = json.loads(r.content.decode('utf-8'))

achievement['book_cnt'] = len(book_list)

# %% 获取：读书笔记xx字
# 在线：不容易很好的获取"读书库"的文本内容
# 因此在另一个库里面计算字数，这里直接引用进来


r = requests.get('https://www.guofei.site/reading/media/reading_words.svg')

soup = BeautifulSoup(r.text, 'lxml')
achievement['reading_words'] = soup.svg.text.strip()

#%% 获取博客数量

r = requests.get('https://www.guofei.site/pages/blog_cnt.svg')

soup = BeautifulSoup(r.text, 'lxml')
achievement['blog_cnt'] = soup.svg.text.strip()

# %% 写入
with open('achievement.json', 'w') as f:
    json.dump(achievement, f, ensure_ascii=False, indent='')
