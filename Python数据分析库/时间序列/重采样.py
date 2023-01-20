import pandas as pd
import numpy as np

a = pd.date_range('2022.7.8', periods=30)
b = pd.Series(np.arange(30), index=a)
# print(b)
# 重采样方法
c = b.resample('W-MON').mean()
d = b.resample('W-MON', closed='right').mean()
# print(f'{c}\n{d}')
# 降采样
dt_time = pd.date_range('2021-8-1', periods=30)
dt_num = np.random.rand(30)
dt_ser = pd.Series(dt_num, index=dt_time)
# print(dt_ser)
dt_resample = dt_ser.resample('7D').ohlc()
# print(dt_resample)
# 升采样
data_demo = np.array([['101', '210', '150'], ['330', '460', '580']])
date_index = pd.date_range('2020/06/10', periods=2, freq='W-SUN')
time_df = pd.DataFrame(data_demo, index=date_index,
                       columns=['A产品', 'B产品', 'C产品'])
print(time_df)
tdf = time_df.resample('D').asfreq()
tdff = time_df.asfreq('D')
print(tdff, type(tdff))
print(tdf, type(tdf))
# 填充数据
print(f'{tdf.ffill()}\n{tdf.bfill()}')
