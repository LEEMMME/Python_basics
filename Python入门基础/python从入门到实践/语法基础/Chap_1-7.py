#  第二章：变量与数据简单类型
# # 变量命名
# message = 'hello world'
# print(message)

# message = 'hello python world'
# print(message)

# # 修改字符串大小写
# name = 'I love lzh python .PY'
# print(name.title())
# print(name.upper())
# print(name.lower())

# 字符串（f字符串）中使用变量
# first_name = 'stenphy'
# last_name = 'curry'
# full_name = f'{first_name} {last_name}'
# a = 'hello'
# print(full_name)
# print(f' hello, {full_name.title()}!')  # 花括号{}内只能放 ‘变量’（如a, full_name）
# print(f'{a} {full_name.title()}!')
# print('hello,', full_name.title(), "!")
# type1 = f'{full_name.title()}'         # f'{ 变量 }'类型为 str（字符串）
# print(type(type1))

# 使用制表符或换行符添加空白

# print('languages:\npython\nc\njava\nc++')   # 换行符 \n
# print('languages:\n\tpython\n\tc\n\tjava\n\tc++')  # 制表符 \t (添加空白)

# 删除空白
# best_language = ' python '
# best_language = best_language.rstrip()  # 删除结尾空白
# print(best_language)
# best_language = best_language.lstrip()  # 删除开头空白
# print(best_language)
# best_language = best_language.strip()   # 删除开头和结尾空白
# print(best_language)

# 动手试一试

# 2-3
# first_name ='stenphy'
# last_name = 'curry'
# full_name = f'{first_name} {last_name}'
# message = f'hello {full_name.title()},would you like to learn python with me!'
# print(message)

# 2-4
# first_name = 'klay'
# last_name = 'thompson'
# full_name = f'{first_name} {last_name}'
# print(full_name.title())
# print(full_name.upper())
# print(full_name.lower())
#
# # 2-5 print('Albert Einstein once said,"A person who never made a mistake
# never tried anything new"')

# 2-6 first_name = 'Albert' last_name = 'Einstein' famous_person = f'{
# first_name} {last_name}' message = 'once said,"A person who never made a
# mistake never tried anything new"' messages = f'{famous_person} {message}'
# print(messages)

#  列表添加（append）、删除（del ）、插入（insert）、修改

# motorcycle = ['honda', 'yamaha', 'suzuki']
# motorcycle.insert(0, 'ducati')
# print(motorcycle)
#  del 删除元素 'ducati'

# del motorcycle[0]
# print(motorcycle)
#  pop() 弹出末尾值

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)               # 将选定的值弹出并赋值，在原列表间接"删除"。
# #  pop() 弹出任意值

# popped_motorcycles_1 = motorcycles.pop(0)
# print(motorcycles)
# #  remove() 删除值

# motorcycles.remove('yamaha')
# print(motorcycles)

# sort() 与 sorted() 排序函数的使用

#    sort()使用
# car = ['bmn', 'audi', 'toyota', 'subaru']
# car.sort()
# print(car)           # 默认升序 reverse=False
# car.sort(reverse=True)   # 降序 reverse=True
# print(car)

#    sorted()的使用
# cars = sorted(car)
# print(cars)
# cars = sorted(car, reverse=True)
# print(cars)

#  for循环

# for number in range(6):
#     print(number)
# #  数值列表
# squares = []       # 创建一个空列表，利用append()把元素添加进列表
# for value in range(1, 11):
#     values = value ** 2       # 次方在python中用 **
#     squares.append(values)
#
# print(squares)

# 列表切片

# list_1 = [number for number in range(7)]
# print(list_1[:3])       # 切片
# message_1 = f'The first three items in the list are:\n{list_1[:3]}'
# print(message_1)
# print('\n')
# print(list_1[-3:])      # 反向索引 切片
# message_2 = f'The last three items in the list are:\n{list_1[-3:]}'
# print(message_2)

#  元组------不可修改的值
# 但是可以为 元组的变量 重新赋值

# 字典
# alien_0 = {}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'   # 添加键值对到空白字典
# # 记录原始位置
# print(f"Original_position:{alien_0['x_position']}")
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# # 新位置是旧位置加上移动距离
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New_position:{alien_0['x_position']}")
#
# print(alien_0)
# del alien_0['speed']   # 删除“speed”
# print(alien_0)
# alien_0['speed'] = 'fast'  # 修改“speed”
# print(alien_0)
#   使用 get() 访问值
# alien_1 = {'color': 'green', 'speed': 'slow', 'points': 3}
# point_value = alien_1.get('points', 'No points value assigned.')
# # 获取points,无points则去默认值
# print(f'{point_value}')

# 遍历字典
# 40个头，100只脚

# 遍历字典
# 遍历字典的所有 键值对
# user_0 = {'user_1': 'curry', 'user_2': 'green', 'user_3': 'klay'}
# for user, value in user_0.items():  # 取两个变量储存字典的 '键'和'值'
#     print(f"key:{user}")            # items 返回一个 键值对 列表
#     print(f"value:{value}\n")
#  遍历字典中所有的键
# user_x = {'user_1': 'poole', 'user_2': 'red', 'user_3': 'colors'}
# for name in user_x.keys():       # 遍历字典时 默认 遍历所有的 键
#     print(f'the_keys:{name.title()}')
# #   排序遍历出的 字典 的 键
# for name in sorted(user_x.keys()):
#     print(f'the_keys:{name.title()}')
# 遍历字典所有的值
# user_y = {'user_1': 'poole',
#           'user_2': 'red',
#           'user_3': 'colors',
#           'user_4': 'red'}
# for names in user_y.values():
#     print(f'the value:{names.title()}')
# # set() 提取一个不重复的列表
# print('\n')
# for names in set(user_y.values()):
#     print(f'the value:{names.title()}')
# while 循环和用户输入

# num = 4 % 3  # % 指出余数
# print(num)

# while 1 == 1:  # 重复问题
#     names = input('So, could you tell me your name?\n')
#     while names != 'curry':
#         print(f'Go out {names}!')
#         break  # 结束循环，返回问题
#     else:
#         print(f'hello\t{names}!')
#         continue  # 继续程序，并返回问题
# list_1 = [1, 2, 3, 4]
# list_2 = []
# while list_1:
#     current_user = list_1.pop()  # 弹出值，添加到list_2
#     print(current_user)
#     list_2.append(current_user)
# print(f'\n{list_2}')
