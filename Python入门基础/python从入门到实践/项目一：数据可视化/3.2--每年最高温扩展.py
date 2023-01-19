import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dtm

data_ = pd.read_csv('sitka_weather_2018_simple.csv')
print(data_)
# 整理数据
t_max = data_[:]['TMAX']
date = data_[:]["DATE"]
t_min = data_[:]["TMIN"]
# 空列表
max_ = []
date_ = []
min_ = []
# 遍历
for x in t_max:
    max_.append(x)

for y in date:
    m = dtm.strptime(y, '%Y-%m-%d')
    date_.append(m)

for z in t_min:
    min_.append(z)

plt.style.use('seaborn')
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111)
ax.plot(date_, max_, c='c', label='每日最高温', alpha=0.5)
ax.plot(date_, min_, c='r', label='每日最低温', alpha=0.5)
# 图标区域着色---------alpha 可见度，默认值（1）为完全可见
ax.fill_between(date_, max_, min_, facecolor='red', alpha=0.1)
plt.title('2018年7月每日最高温度')
plt.xlabel('日期', fontsize='18')
plt.ylabel('温度', fontsize='18')

# 中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 展示
plt.legend()
plt.show()
