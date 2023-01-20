import matplotlib.pyplot as plt
import numpy as np
# 创建画布
fig = plt.figure(figsize=(12, 8))
# 创建子图
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(212)
# 创建数据
x1 = ['apple', 'banana', 'orange', 'vegetable']
y1 = [12, 23, 18, 21]
ax2_color = ['pink', 'c', 'm', 'orange']
x3 = np.linspace(0.001, 10, 100)
y3 = np.sin(10*x3)/x3
# 绘图
ax1.barh(x1, y1, color='c')
ax2.pie(y1, explode=[0, 0.1, 0, 0], labels=x1, colors=ax2_color)
ax3.plot(x3, y3, color='pink', lw=3, marker='*', markersize='12',
         markerfacecolor='c')
# 展示绘图
plt.show()