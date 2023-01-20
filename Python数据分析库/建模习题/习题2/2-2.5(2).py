import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection='3d')
x = np.linspace(-2, 2, 100)
y = np.linspace(-6**(1/2), 6**(1/2), 100)
x, y = np.meshgrid(x, y)
z = x**2/4+y**2/6
ax.plot_surface(x, y, z)
plt.show()
