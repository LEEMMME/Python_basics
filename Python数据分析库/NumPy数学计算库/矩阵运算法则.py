import numpy as np
# 简单几何运算
a = np.array([[0, 3, 4], [1, 6, 4]])
b = np.array([[1, 2, 3], [2, 1, 4]])
c = a / b   # 两个矩阵对应元素相除
# print(c)
d = np.array([[2, 3, 2], [1, 1, 1]])
e = a * d   # d先广播成与a同维数的矩阵，再逐个元素相乘
# print(e)
f = np.array([[3], [2]])
g = f * a   # f先广播成与a同维数的矩阵，再逐个元素相乘
# print(g)
h = a ** (1/2)  # a矩阵逐个元素的1/2次幂
# print(h)

a = np.ones(4)
b = np.arange(2, 10, 2)
print(a)
print(b)
ab = a @ b  # a作为行向量, b作为列向量
print(ab)
d = np.arange(16).reshape(4, 4)
print(d)
f = a @ d  # a作为行向量
print(f)
df = d @ a  # a作为列向量
print(df)
