import json
from bs4 import BeautifulSoup

with open('achievement.json', 'r') as f:
    achievement = json.load(f)

# %% 获取：读书xx本，笔记xx字，博客xx篇，被关注xx次
import requests

r = requests.get('https://www.guofei.site/pages/achievement.json')
achievement_new = json.loads(r.content.decode('utf-8'))
achievement.update(achievement_new)

# %%获取总star
r = requests.get('https://www.guofei.site/pages/cnt_github_repo.json')
github_repo = json.loads(r.content.decode('utf-8'))

achievement["github_total_star"] = sum(i["stargazers_count"] for i in github_repo)
achievement["github_total_star_str"] = str(round(achievement["github_total_star"] / 1000, 1)) + "k"
achievement["github_total_fork"] = sum(i["forks_count"] for i in github_repo)

# %% 写入
with open('achievement.json', 'w') as f:
    json.dump(achievement, f, ensure_ascii=False, indent='')
