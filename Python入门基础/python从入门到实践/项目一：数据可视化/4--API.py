import requests
from plotly.graph_objs import bar
from plotly import offline
import pylab
# 执行API调用并储存响应
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code :{r.status_code}')
# 将API响应赋给一个变量
response_dict = r.json()
# 处理结果
print(response_dict.keys())
print(f"Total repositories:{response_dict['total_count']}")
# 探索有关仓库信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")
# 研究第一个仓库

# repo_dict = repo_dicts[0]
"""
print(f"\nkeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
"""

print("\nSelected information about each repository:")
# 遍历，涵盖多个库的信息
"""
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
"""
# 绘图(Plotly仓库)
links = []
stars = []
labels = []
for repo_dict in repo_dicts:
    name = repo_dict['name']
    url_ = repo_dict['html_url']
    link = f"<a href='{url_}'>{name}</a>"
    links.append(link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
# 可视化
data = [{
    'type': 'bar',
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'red',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'GitHub最受欢迎的仓库',
    'xaxis': {
        'title': '仓库名称',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '推荐星数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {
    'data': data,
    'layout': my_layout,
}
offline.plot(fig, filename='GitHub_python.html')

