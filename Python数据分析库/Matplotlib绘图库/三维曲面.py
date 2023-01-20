import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm  # 颜色映射
# -------------------
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection="3d")
# -------------------
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = np.sin((x**2+y**2)**(1/2))
# -------------------
ax.plot_surface(x, y, z, cmap=cm.cool)
# -------------------
plt.show()
