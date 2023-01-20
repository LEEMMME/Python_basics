from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
# 一维插值
x1 = np.arange(0, 10, 0.1)
y1 = np.sin(x1)
print(x1)
func_n = interp1d(x1, y1)

nx = np.arange(0, 9, 0.1)
ny = func_n(nx)
plt.plot(x1, y1,'p',nx,ny,'-.')
plt.show()
