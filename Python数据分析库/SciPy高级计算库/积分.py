# 一重积分
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def point(x):
    return np.cos(x)


final = quad(point, 0, np.pi/4)
print(final)

