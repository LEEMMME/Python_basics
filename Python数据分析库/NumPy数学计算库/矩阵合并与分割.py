import numpy as np

# 创建一维数组
a = np.array([1, 2, 3, 4]).reshape(2,2)
a_ = np.array([2, 1, 6, 7]).reshape(2,2)
# 创建三维数组
b = np.arange(0, 16).reshape((2, 4, 2))
# 合并
c1 = np.hstack((a, a_))  # 水平合并
c2 = np.vstack((a, a_))  # 垂直合并
c3 = np.dstack((a, a_))  # 三维合并
print(c1)
print(c2)
print(c3)
# 拆分
c11 = np.hsplit(c1,2)
c22 = np.vsplit(c2,4)
c33 = np.dsplit(c3,2)
print(c11[0])
print(c22)
print(c33[0])