import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
dt = np.random.random(365)
dt_index = pd.date_range('2021-1-1', '2021-12-31', freq='D')
dt_series = pd.Series(dt, index=dt_index)
print(dt_series)
ds = dt_series.rolling(window=10)
print(ds)
print(ds.max())
# 绘图

dt_series.plot(style='y--')
ds.mean().plot(style='b')
plt.show()

