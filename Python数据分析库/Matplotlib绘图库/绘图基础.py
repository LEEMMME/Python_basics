# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()
# plt.plot(x, y, c='red', lw=1, ls='-', marker='o', markersize=3,
#          markeredgecolor='green', markerfacecolor='green')
# plt.show()
# deferred_rendering.py
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(0)
# x = np.random.rand(20)
# y = np.random.rand(20)
#
# area = (50 * np.random.rand(20)) ** 2
#
# plt.scatter(x, y, s=area, alpha=0.5)
# plt.title('Scatter')
# plt.show()
# data_y = np.array([12, 23, 34, 45])
# data_x = range(4)
# data_y2 = np.array([11, 22, 33, 44])
# plt.bar(data_x, data_y, width=0.4, label='second')
# plt.plot(data_x, data_y2, c='red', lw=2, ls='-', label='first')
# plt.legend()
# plt.show()


# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 定义标签
# sizes = [15, 23, 35, 10]  # 每一块的比例
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  # 每一块的颜色
# explode = (0, 0.1, 0, 0)  # 突出显示，这里仅仅突出显示第二块（即'Hogs'）
#
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# autopct='%.2f%%', shadow=True, startangle=90)
# plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
# plt.show()
# 三维绘图
# 导入模块
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# # 创建画布
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
# # 导入数据
# z = np.linspace(0, 20, 1000)
# y = 5*np.cos(z)
# x = 5*np.sin(z)
# _z = 20*np.random.random(100)
# _x = 5*np.sin(_z)
# _y = 5*np.cos(_z)
# # 绘画曲线图
# ax.plot(x, y, z, color='orange')
# # 绘画散点图
# ax.scatter(_x, _y, _z, color='c', marker='p', s=100, edgecolor='g')
# # 添加标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# # 解决中文乱码
# plt.rcParams['font.sans-serif'] = ['SimHei']
# # 解决负号显示问题
# plt.rcParams['axes.unicode_minus'] = False
# # 添加标题
# ax.set_title('散点环绕曲线')
# # 显示图像
# plt.show()
# a, b, c = 10., 28., 8. / 3.
# def lorenz_map(x, dt=1e-2):
#     x_dt = np.array([a * (x[1] - x[0]), x[0] * (b - x[2]) - x[1], x[0] * x[1] -
#                      c * x[2]])
#     return x + dt * x_dt
#
#
# points = np.zeros((8000, 3))
# x = np.array([.1, .0, .0])
# for i in range(points.shape[0]):
#     points[i], x = x, lorenz_map(x)
#
# # Plotting
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
# ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))
# ax.plot(points[:, 0], points[:, 1], points[:, 2], c='c')
# plt.show()
# from numpy import ma
#
# lon = np.linspace(-180, 180, 37)
# lat = np.linspace(-90, 90, 19)
# lons = np.meshgrid(lon)
# lats = np.meshgrid(lat)

# 爱心
# def love_s(i, a, b, c):
#     s = np.array(np.sqrt(a-np.power((abs(i)-b), c)))
#     return s
#
#
# def love_t(i, a, b, c):
#     t = -a*np.sqrt(b-c*abs(i))
#     return t
#
#
# if __name__ == '__main__':
#     i = np.linspace(-2, 2, 100)
#     x = love_s(i, 1, 1, 2)
#     y = love_t(i, 2, 1, 0.5)
#
#     plt.plot(i, x, '--')
#     plt.plot(i, y, '--')
#     plt.show()

import numpy as np
import matplotlib.pyplot as plt
# 整理数据

days = np.array(['一月', '二月', '三月', '四月', '五月', '六月'])
data_x1 = np.array([13, 10, 27, 33, 30, 45])
data_x2 = np.array([1, 10, 7, 26, 20, 25])
# 作图
fig = plt.figure(figsize=(6, 6), edgecolor='lightgreen')  # 做画布
plt.plot(days, data_x1, ls='--', lw=4, c='c', marker='p', label='钻石销量')
plt.plot(days, data_x2, lw=2, ls='-.', c='m', marker='x',
         label='铂金销量')
# 添加标签
plt.xlabel('月份', fontsize=20)
plt.ylabel('每月销量', fontsize=20)
# 中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 显示标签
plt.legend()
# 展示
plt.show()