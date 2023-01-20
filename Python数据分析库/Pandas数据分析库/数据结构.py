import pandas as pd
import numpy as np
data = [1, 2, 3, 4, 5]
p_data = pd.Series(data)

data1 = pd.DataFrame(np.arange(8).reshape(2, 4), index=list('ab'),
                     columns=list('WERT'))
# print(data1)
data1.loc['a', 'E'] = np.nan
data1.iloc[1, 2] = np.nan
print(data1)
print(data1.notna())
# print(type(data1.loc['a', 'E']))
# data1.dropna(axis=0, how='all', inplace=True)
# data1.dropna(axis=1, how='any', inplace=True)
print(data1.mean())
data1.fillna(data1.mean(), inplace=True)

print(data1)

pt = pd.read_csv('dog_name.csv')
# print(type(pt))
# print(pt, '\n')
# print(pt.head(3))
# print(pt.tail(2))
# print(pt.info())
# print(pt.describe())
# print(pt[:4]["age"])
# print(pt.loc[[1,3],'age'])
# print(pt.iloc[[1, 3],0:1])
# print(pt[(pt['age'] > 20) ^ (pt['age'] < 100)].dogname)
pt.sort_values(by='age', ascending=False, inplace=True)
pt.loc[[2, 4], 'age'] = np.nan
# print(pt)
# print(pt[2:3]['age'])
# print(pt.loc[2, 'age'])
# print(pt.iloc[2, 1])
# print(pd.isnull(pt))
# print(pd.notnull(pt))

