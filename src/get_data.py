import json
from bs4 import BeautifulSoup

with open('achievement.json', 'r') as f:
    achievement = json.load(f)

# %% 获取：读书xx本，笔记xx字，博客xx篇，被关注xx次
import requests

r = requests.get('https://www.guofei.site/pages/achievement.json')
achievement_new = json.loads(r.content.decode('utf-8'))
achievement.update(achievement_new)



# %% 写入
with open('achievement.json', 'w') as f:
    json.dump(achievement, f, ensure_ascii=False, indent='')
