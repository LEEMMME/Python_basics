import matplotlib.pyplot as plt
import numpy as np
# 画布，子图，三维模式
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot(211, projection="3d")
ax2 = plt.subplot(212, projection='3d')
# 创建数据
z = np.linspace(-50, 50, 1000)
x = z**2*np.sin(z)
y = z**2*np.cos(z)
# ——————————————————————————————————————ax2为曲面
x2 = np.linspace(-10, 10, 100)
y2 = np.linspace(-10, 10, 100)
x2, y2 = np.meshgrid(x2, y2)
z2 = 50*np.sin(x2+y2)
# 绘图
ax1.plot(x, y, z, 'c')
ax2.plot_surface(x2, y2, z2)
# 展示
plt.show()