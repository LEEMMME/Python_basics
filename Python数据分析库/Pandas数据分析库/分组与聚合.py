import pandas as pd
import numpy as np

# 重塑数据
dic1 = {'key': ["1", "k1", "k2"], 'A': ['A0', 'A1', 'A2'],
        'B': ['B0', 'B1', 'B2']}
dic2 = {'key': ["k0", "k1", "k2", "k3"], 'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'], 'C': ["C0", 'C1', "C2", 'C3']}
dc1 = pd.DataFrame(dic1)
dc2 = pd.DataFrame(dic2).T
# print(dc2)
# 转换格式
# print(dc1.unstack())
# 重命名行或列索引
dc1.rename(columns={'key': 'W'}, inplace=True)
# print(dc1)
z = '我爱你China'
q = z.replace('China', '中国')
# print(q)
# 分组与聚合
pf = pd.read_csv('D:/BaiduNetdiskDownload/DataAnalysis-master/day05/code'
                 '/starbucks_store_worldwide.csv')
# 显示所有列
pd.set_option('display.max_columns',None)
# 显示所有行
pd.set_option('display.max_rows',None)
# print(pf.head(1))
# print(pf.info())
grouped = pf.groupby(by=[pf['Country'], pf['State/Province']])[
    'Brand'].count()
# print(grouped)
# for brand in grouped:
#     print(brand)

# dt = pf[pf['Country'] == 'CN']
# group = dt.groupby('State/Province')['Brand'].count()
# print(group)
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar',
      'foo', 'foo'],'B' : ['one', 'one', 'one', 'one','two', 'two',
      'two', 'two'],'C' : np.arange(1,9),'D' : np.arange(6,14)})
# print(df)
# df.set_index(['B', 'A'], inplace=True)
# print(df)
# print(df.loc['two'].loc['foo'])
# print(df.swaplevel())
dgb = df.groupby(by='B').agg({'A': 'count','C':['sum','max','min'],
                              'D':['sum','max','min']})
# print(dgb)
# fg = df.groupby(by='B')
# for hj,o in fg:
#     print(f'\n{hj}:')
#     print(o)
# a = {'a': [2, 3, 4, 5, 8], 'b': [23, 12, 21, 13, 19],
# 'c': [6, 17, 20, 11, 14]}
# d_f = pd.DataFrame(a).agg(sum, axis=1)
# print(d_f)
