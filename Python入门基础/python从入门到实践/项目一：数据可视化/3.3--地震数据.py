import json
import plotly.express as px
import pandas as pd
# file = 'eq_data_1_day_m1.json'
file = 'eq_data_30_day_m1.json'
with open(file, 'r') as f:
    eq_dt = json.load(f)
# _file = 'D:/readable data.json'
"""
_file = 'D:/30day data.json'
with open(_file, "w") as f:
    json.dump(eq_dt, f, indent=4)
"""
# 处理数据
features = eq_dt['features']
mags, titles, lons, lats = [], [], [], []
for x in features:
    mag = x['properties']['mag']
    title = x['properties']['title']
    lon = x['geometry']['coordinates'][0]
    lat = x['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
# 绘制地震散点图
"""
fig = px.scatter(
                 lons, lats,
                 labels={'x': '经度', 'index': '纬度'},
                 title='全球地震散点图',
                 range_x=[-200, 200],
                 range_y=[-190, 190])
fig.write_html('global.html')
fig.show()
"""
# 绘制2.0(定制标记尺寸)
"""
data = pd.DataFrame(zip(mags, titles, lons, lats), columns=['震级', '位置', '经度',
                                                            '纬度'])
fig = px.scatter(
                 data,
                 x='经度',
                 y='纬度',
                 title='全球地震散点图',
                 range_x=[-200, 200],
                 range_y=[-190, 190],
                 size='震级')
fig.write_html('global-2.0.html')
fig.show()
"""
# 绘制3.0(定制标记颜色)
data = pd.DataFrame(zip(mags, titles, lons, lats), columns=['震级', '位置', '经度',
                                                            '纬度'])
fig = px.scatter(
                 data,
                 x='经度',
                 y='纬度',
                 title='全球地震散点图',
                 range_x=[-200, 200],
                 range_y=[-190, 190],
                 size='震级',
                 color='震级',
                 hover_name='位置')
fig.write_html('global-3.0.html')
fig.show()
