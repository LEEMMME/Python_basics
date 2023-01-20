import pandas as pd
import numpy as np
# 数据合并
# NO.1 函数 concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
#        keys=None, levels=None, names=None, verify_integrity=False, copy=True):
# 创建数据(NO.1 and NO.2)
dt1 = pd.DataFrame(np.arange(0, 12).reshape((3, 4)), index=list('abc'),
                   columns=list('xyzq'))
dt2 = pd.DataFrame(np.arange(4, 10).reshape((2, 3)), index=list('be'),
                   columns=list('jkl'))
# 合并数据
dt_12 = pd.concat([dt1, dt2])
dt_21 = pd.concat([dt1, dt2], axis=1)
dt_12_3 = pd.concat([dt1, dt2], join='inner')
dt_21_3 = pd.concat([dt1, dt2], axis=1, join='inner')
# print(dt1, '\n', dt2, '\n', dt_12, '\n', dt_12_3,
#       '\n', dt_21, '\n', dt_21_3)
# NO.2 函数join(self, other, on=None, how='left', lsuffix='',
#                                     rsuffix='',sort=False): 只能按列合并
# 合并数据
da = dt1.join(dt2, how='right')
# print(da)
# NO.3 函数 merge(left, right, how='inner', on=None, left_on=None, right_on=None,
#       left_index=False, right_index=False, sort=True,
#       suffixes=('_x', '_y'), copy=True, indicator=False)
# 创建数据(NO.3)
dic1 = {'key': ["k0", "k1", "k2"], 'A': ['A0', 'A1', 'A2'],
        'B': ['B0', 'B1', 'B2']}
dic2 = {'key': ["k0", "k1", "k2", "k3"], 'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'], 'C': ["C0", 'C1', "C2", 'C3']}
dc1 = pd.DataFrame(dic1)
dc2 = pd.DataFrame(dic2)
print(dc1)
# print(dc2)
# 合并数据
dc2.loc[2, 'key'] = 'k4'
dc2.loc[2, 'B'] = 'k6'
# dc2.loc[3, 'key'] = 'k2'
print(dc2)
do = pd.merge(dc1, dc2, left_on='key', right_on='key', how='inner')
print(do)
dt = pd.merge(dc1, dc2, how='outer')
df = pd.merge(dc1, dc2, how='outer', left_index=True, right_index=True)
# print(dt1)
# print(dt2)
# print(df)
# print(dt)
# NO.4  data.append(self, other, ignore_index=False, verify_integrity=False,
# sort=False)
