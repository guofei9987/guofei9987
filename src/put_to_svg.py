
import json


with open('data/book_cnt.svg', 'w') as f:
    with open('achievement.json') as f2:
        achievement = json.load(f2)


    f.write('''<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="58" height="22" role="img">
  <text x="1" y="20" style="fill:red;">{}本
  </text>
</svg>'''.format(achievement['cnt_book']))