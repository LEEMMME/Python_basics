from random import choice
import matplotlib.pyplot as plt


# 创建类
class RandomWalk:
    """生成一个随机漫步的类"""

    def __init__(self, num_points=5000):
        """初始化类的属性"""
        self.num_points = num_points
        # 所有漫步都始于（0，0）
        self.x_value = [0]
        self.y_value = [0]

    def random_walk(self):
        """计算所有漫步包含的所有点"""

        # 不断地漫步，知道列表达到指定长度
        while len(self.y_value) < self.num_points:

            # 决定前进的方向与距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_distance*x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个x,y值
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)


# 绘制随机漫步图
rw = RandomWalk()
rw.random_walk()
# 使用内置样式
plt.style.use('classic')
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111)
numbers = range(rw.num_points)
ax1 = ax.scatter(rw.x_value, rw.y_value, c=numbers, cmap=plt.cm.Blues,
                 marker='x')
# 重点标记起点和终点
ax.scatter(0, 0, c='green', s=100)
ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=100)
# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# 添加渐变条
plt.colorbar(ax1)
plt.show()

