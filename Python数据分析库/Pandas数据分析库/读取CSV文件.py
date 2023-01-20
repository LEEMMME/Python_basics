import pandas as pd
path = 'D:/Python数学建模库/Pandas数据分析库/file_path.csv'
pd = pd.read_csv(path)
print(pd)
a = pd.iloc[1, 2]
print(a)
print(pd.describe().round(2))  # round()保留几位小数
