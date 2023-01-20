import pandas as pd
from datetime import datetime
import numpy as np
# 创建时间序列
a = pd.to_datetime('20220808')
b = pd.to_datetime(['20220808', '20210808', '20210909', '20200808', '19980909'])
print(b)
print(type(b), '\n', '-'*40)

# 创建时间序列类型的Series对象
dt = pd.Series([11, 23, 34, 45, 56], index=b)
print(dt)
print("*"*40)
# 索引获取子集
print(dt[1])  # no.1
print(dt['20200808'])  # no.2
datetime = datetime(2020, 8, 8)  # no.3 ,datetime对象
print(dt[datetime])
print(dt['2021'])  # 获取某年数据

# truncate(before = None,after = None,axis = None,copy = True)
# before – 表示截断此索引值之前的所有行。
# after – 表示截断此索引值之后的所有行。
# axis – 表示截断的轴，默认为行索引方向。
dt.sort_index(inplace=True)
print(dt)
dt = dt.truncate(after='2020-08-08')
print(dt)