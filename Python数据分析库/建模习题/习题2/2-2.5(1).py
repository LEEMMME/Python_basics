import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(-np.pi / 2, np.pi / 2, 50)
u, v = np.meshgrid(u, v)
x = 2 * np.cosh(v) * np.cos(u)
y = np.sqrt(10) * np.cosh(v) * np.sin(u)
z = 2 * np.sqrt(2) * np.sinh(v)
ax.plot_surface(x, y, z, cmap='Blues')
plt.show()

