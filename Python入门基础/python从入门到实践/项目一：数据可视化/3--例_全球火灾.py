import csv

import pandas as pd
import plotly_.express as px
with open('world_fires_1_day.csv') as f:
    reader = csv.reader(f)
    rows = next(reader)
    print(rows)
    # 经纬度
    lats = []
    lons = []
    brns = []
    for row in reader:
        lat = row[0]
        lon = row[1]
        brn = row[2]
        lons.append(lon)
        lats.append(lat)
        brns.append(brn)
# 绘图
# fig = px.scatter(lats, lons, labels={'x': '经度', 'index': '纬度'},
#                  title='全球火山散点图')

data = pd.DataFrame(zip(lons, lats, brns), columns=['经度', '纬度', '亮度'])
fig = px.scatter(data, x='经度', y='纬度', title='全球火山散点图', color='亮度')
fig.write_html('world fires.html')
fig.show()
