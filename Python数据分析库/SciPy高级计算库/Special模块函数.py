import scipy.special as sl
import numpy as np
import matplotlib.pyplot as plt
# 伽马函数-gamma
x = np.linspace(-5, 5, 1000)
y = sl.gamma(x)
plt.plot(x,y)
plt.show()
