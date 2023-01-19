import random
from plotly_.graph_objs import Bar, Layout
from plotly_ import offline


# 创建类
class Die:

    def __init__(self, number=6):
        self.number = number

    def rolls(self):
        return random.randint(1, self.number)


D6 = Die()
D6_2 = Die()
# 投掷100次的结果
results = []
for x in range(100):
    result = D6.rolls() + D6_2.rolls()
    results.append(result)
print(results)
# 各个点/面出现的次数
fre = []
for x in range(2, D6_2.number+D6.number+1):
    num = results.count(x)
    print(x)
    fre.append(num)
print(fre)
# 绘制直方图
x_value = list(range(2, D6_2.number+D6.number+1))
data = [Bar(x=x_value, y=fre)]
x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
_layout = Layout(title='投掷两个D6100次的结果', xaxis=x_axis_config,
                 yaxis=y_axis_config)
offline.plot({'data': data, 'layout': _layout}, filename='d6_2-.html')
