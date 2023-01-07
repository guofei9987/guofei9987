import requests

import json

with open('achievement.json', 'r') as f:
    achievement = json.load(f)

about_url = 'https://raw.githubusercontent.com/guofei9987/guofei9987.github.io/master/pages/about.md'

r = requests.get(about_url)

content = r.content.decode('utf-8') \
    .replace('''---
layout: page
title: 关于
---

''', '') \
    .replace('{{ site.posts.size }}', achievement['cnt_blog']) \
    .replace('{{ site.data.cnt_reading_words.cnt_reading_words }}', achievement['cnt_reading_words']). \
    replace('{{ site.data.book_list.size }}', 'cnt_book') \
    .replace('''我的项目：

<table>
<tr>
  <th>Project</th>
  <th>Star</th>
  <th>Fork</th>
  <th>description</th>
</tr>

{% assign sorted_repos = (site.github.public_repositories | sort: 'stargazers_count') | reverse | where: "fork", "false" %}
{% for repo in sorted_repos | limit: site.side_bar_repo_limit %}
<tr>
  <td><a href="{{ repo.html_url }}">{{ repo.name }}</a></td>
  <td>{{ repo.stargazers_count }}</td>
  <td>{{ repo.forks_count }}</td>
  <td>{{ repo.description | truncate:30 }}</td>
</tr>
{% endfor %}
</table>''', '')
# 这个暂时先这样

with open('README.md', 'w') as f:
    f.write(content)
