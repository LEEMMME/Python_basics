# %%  简单问候函数
def greet(username):
    # 简单的问候语
    print(f'hello {username.title()}\n')


greet('curry')  # username是形参，curry是实参


# %%  食物及数量函数
def food_message(types, number):  # 位置实参
    print(f'食物名称：{types.title()}')
    print(f'食物数量：{number}\n')


food_message('bread', 4)  # 实参与形参顺序相同
food_message(types='chicken', number=2)  # 关键词实参


# %%  宠物类型及名字函数
def pet_list(pet_type='dog', pet_name='marry'):  # 给形参指定默认值
    print(f'宠物类型：{pet_type.upper()}')
    print(f'宠物名字：{pet_name.title()}\n')


pet_list()  # 实参为 空值 时打印默认值


# %%  最喜欢的书籍
def fav_book(book='野草'):
    best_book = f'我最喜欢的书籍是：{book.title()}'
    return best_book  # 返回值best_name


books = fav_book('狂人日记')  # 调用返回值的函数时，提供一个变量赋给返回的值
print(books)


# %%
def names(first_name, final_name, age=None):  # 可选择值，即将其默认值设为空
    full_name = {'first_name': first_name, 'last_name': final_name}
    # 判定age是否为空，空 为false
    if age:
        full_name['age'] = age
    return full_name


finals = names('stephen', 'curry', 12)
print(finals)


# %%
def show_messages(no_print_list):
    print('All the value:')
    for messages in no_print_list:
        print(f'\t{messages}')


def send_messages(no_print_list, printed_list):
    no_print_lists = no_print_list[:]  # 创建副录，保持原列表不变
    while no_print_lists:  # pop()只对列表作用，字符串不可以
        current_value = no_print_lists.pop()  # 所以用while循环
        print(f'弹出的值：{current_value}')
        printed_list.append(current_value)  # 导入弹出值到空列表
    print(f'未打印的值：\n\t{no_print_lists}')
    print(f'打印完成的值：\n\t{printed_list}')


list_1 = ['red', 'yellow', 'orange']
list_2 = []
show_messages(list_1)
send_messages(list_1, list_2)


# %%
def make_cars(manufacturer, model, **kwargs):  # 一个星号是建立空元组，两个建立空字典
    kwargs['manufacturers'] = manufacturer
    kwargs["models"] = model
    return kwargs


cars = make_cars('aa', 'kk', curry='www')
print(cars)
