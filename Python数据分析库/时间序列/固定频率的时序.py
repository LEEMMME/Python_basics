import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import *
import numpy as np
# 创建datetimeindex对象
dt_range = pd.date_range('20210808', '20220808', freq='W-SUN',
                         tz='Asia/Shanghai',normalize=True)
# print(dt_range)

# 时间序列的频率、偏移量
a = DateOffset(months=5)  # 偏移量
b = Week(1) + Hour(10)
print(a)
data_time = pd.date_range('2021-8-8', '2022-8-8', freq='M')
print(data_time)
dd = pd.Series(np.linspace(0, 12, 12), data_time)
# 时间序列的移动
move = dd.shift(1)
print(move)

