import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dtm

data = pd.read_csv('sitka_weather_07-2018_simple.csv')
# 打印列标
print(data)
t_max = data[:]['TMAX']
date = data[:]["DATE"]
max_ = []
date_ = []
for x in t_max:
    max_.append(x)

for y in date:
    m = dtm.strptime(y, '%Y-%m-%d')
    date_.append(m)

# 绘制温度图
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111)
plt.style.use('seaborn')
ax.plot(date_, max_, c='c', label='每日最高温')
plt.title('2018年7月每日最高温度')
plt.xlabel('日期', fontsize='18')
plt.ylabel('温度', fontsize='18')

# 中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 展示
plt.legend()
plt.show()
