import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
x = np.random.random(100)
y = np.random.random(100)
plt.scatter(x, y, c=range(100), cmap=cm.Blues)
plt.colorbar()  # 颜色映射*
plt.show()