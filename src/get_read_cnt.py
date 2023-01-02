# 获取：读书xx本
import json
import requests

r = requests.get('https://www.guofei.site/pages/book_list.json')

book_list = json.loads(r.content.decode('utf-8'))

# with open('https://www.guofei.site/pages/book_list.json') as f2:
#     book_list = json.load(f2)

# %%
with open('achievement.json', 'r') as f:
    achievement = json.load(f)

achievement['book_cnt'] = len(book_list)

with open('achievement.json', 'w') as f:
    json.dump(achievement, f, ensure_ascii=False, indent='')

