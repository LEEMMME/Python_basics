import pandas as pd
# Period类表示一个标准的时间段或时期，比如某年、某月、某日、某小时等
# 创建Period对象
ppd1 = pd.Period('2022-9')
ppd2 = pd.Period('2022-9-20')
ppd3 = pd.Period('2022')
# Period对象进行计算
print(f'{ppd1+1}\n{ppd2+4}\n{ppd3-2}')
# 相同频率进行计算
ppd1_ = pd.Period('2012-2')
print(ppd1-ppd1_)
# 创建多个Period对象
dx1 = pd.PeriodIndex(['2022-1','1998-9', '2014'], freq='M')
dx2 = pd.period_range('20140908', '20180604', freq='D')
print(f'{dx1}\n{dx2}')
# 时期的频率转换
period = pd.Period('2019', freq='A-DEC')
loi = period.asfreq('M', how='start')
print(loi)
