# %% Dog类
class Dog:  # 定义 类 Dog（首字母大写）
    """第一次模拟小狗的尝试"""

    def __init__(self, name, age):
        self.name = name  # self为前缀的变量可供 类 中的所有方法使用
        self.age = age  # 变量为类的属性

    # 定义 类 中的方法
    def sit(self):
        """模拟狗收到命令时蹲下"""
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        """模拟狗子收到指令翻滚"""
        print(f'{self.name.title()} rolled over.')


# 根据类创建实例my_dog
my_dog = Dog('harry', 6)  # 创建一条名为harry，六岁的小狗
print(f"My dog's name is {my_dog.name.title()}.")  # 访问 类 的属性
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()  # 句点表示法 调用 类 中定义的方法
my_dog.roll_over()


# %% Car类
class Car:
    """模拟一个汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  # 指定默认值

    def control(self):
        wer = f'{self.make} {self.model} {self.year}'
        return wer

    def reading(self):
        odo = f'This car has {self.odometer} miles on it.'
        print(odo)

    def data_odo(self, data1):  # 修改属性的值（定义函数）
        self.odometer = data1
        return self.odometer


my_car = Car('audi', 'a4', 2019)
print(my_car.control())
my_car.reading()
my_car.data_odo(23)
my_car.reading()


# %% 类的继承
class Electric(Car):

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(Electric, self).__init__(make, model, year)


# %% 小餐馆
def open_restaurant():
    print(f'The restaurant is opening now.')


class Restaurant:
    """一个小餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}{self.cuisine_type}')


restaurant = Restaurant('happy day', 'ice_cream')
name = restaurant.restaurant_name
type_ = restaurant.cuisine_type
print(f'\nThe name is {name.title()} and the type is {type_}.')


# %% 冰淇淋
class IceCreamStand(Restaurant):
    """继承父类小餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化小餐馆"""
        super(IceCreamStand, self).__init__(restaurant_name,
                                            cuisine_type)

    def flavors(self):
        taste_list = ['Chocolate', 'Cream', 'Matcha', 'Vanilla']
        return taste_list


# %% 筛子
class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        import random as rd
        choose = rd.randint(1, self.side)
        self.side = choose
        return self.side


died = Die(5)
print(died.side)
print(died.roll_die())
