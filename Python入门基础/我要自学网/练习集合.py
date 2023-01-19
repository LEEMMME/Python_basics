# a=3
# b=2
# c=3
# print(a+b+c)

# name="李志豪"
# age="18岁"
# time="2025年"
# print(name,age,time)
# a="李志豪"
# b="你"
# c="曾经喜欢"
# d=a+"可能"+c+b

# print(d)


# a = "李志豪"
# b="佩服"
# c="钱学森"
# s1="李志豪{}{}{}".format("于敏","~~~","邓稼先")
# print(s1)

# a=True
# b=False

# print(5<8)
# 接受用户数据的变量=input("提示语句")
# number=input("请给你的颜值打个分数1-10分：")
# print("您的颜值分数是：",number)
# print("您的自恋指数是：",int(number)*12.14)
# if 10>int(number)>=8:
# 	print("你以为你是王祖贤吗，脸都不要的啦")
# if 5<=int(number)<8:
# 	print("喂，你对自己还蛮自信耶！可不可以低调一点呀？")
# if 0<int(number)<5:
# 	print("嘿，你要不要这么悲观呀，世界还是很美丽的啦，出去走走嘛，你还没看完大好河山呢！")
# else:
# 	print("请输入正确命令")


# a=9
# b=8
# print(a/b) 
# print(a//b)#只保留整数
# print(a**b)#幂函数

# a+=5
# a-=5   a=a-5,类推
# a*=5
# print(a) 

# a=2
# b=5
# c=5
# print(c==b)
# print(a!=b)
# print(1>5 and 2<5)
# print(2<3 or 8>9)
# print(not 4==4)#与判断结果相反

# 列表
# lista=["张三","李四","王五","刘六"]
# print(lista[0],lista[1])
# print(lista[0:3:2])  #print(lista[起始索引:结束索引(不包括）:索引间隔]#

# #添加索引
# lista=["张三","李四","王五","刘六"]
# lista.append("大宝贝")
# lista.insert(2,"库里")#插入
# #删除索引
# lista.remove("李四")
# lista.pop(2)
# #重新赋值(替代)
# lista[1]="斯蒂芬.库里"
# print(lista)

# 元组，不可修改
# tuplea=(23,23,3,2,32,323,2,3,90)
# print(tuplea[3])
# 二三维容器，数据保密
# lista=[23,3,33,43,43,345,3,4,34,44,3232]#￥列表
# listb=[323,343434,4556,[89,"外滩","金桥"],37,434,85,55,7,]
# listc=["上海",234,2022,"东方明珠",8888,9800]

# listx=(lista,listc,listb,666)#@#元组
# # print(listb[3][2])#二维
# print(listx[2][3][1])#三维

# 字典
# dicta={"name":"zhangsan","age":18,"hobby":"playBall"}

# dicta["name"]="李四"#修改，直接赋值
# print(dicta["name"])
# dicta.pop("name")#删除，pop
# print(dicta)
# dicta["son"]="王五"#增添
# print(dicta)


# 集合
# set,不重复
# seta={3,23,3,4,3,4,5,4,56,3,4,2,32,32,}
# setb={23,34,455,455,5453,2434,2}
# print(seta&setb)#交集
# print(seta|setb)#并集
# print(seta-setb)#差集，前值减共值

# print("z",end="")  不换行end=""
# print("x",end="")
# print()


# a,b=1,2
# print(a,b)


# 1.星期一特价菜：水煮鱼
#   星期二特价菜：烧排骨
#   星期三，四特价菜：宫爆鸡丁
#   星期五，六特价菜：清蒸鲈鱼
#   其它：干锅肥肠
# 根据用户输入星期几，输出特价菜是什么？
# day=int(input("星期几(输入数字）："))
# if day==1:
# 	print("水煮鱼")
# elif day==2:
# 	print("烧排骨")
# elif day==3 or day==4:
# 	print("宫爆鸡丁")
# elif day==5 or day==6:
# 	print("清蒸鲈鱼")
# else:
# 	print("干锅肥肠")
# input("点击enter键退出！")

# 2.根据输入判断学生的成绩等级，
# 如果成绩>=90分，则输出“优秀”;
# 如果成绩>=80分，则输出“良好”;
# 如果成绩>=60分，则输出“中等”;
# 否则，输出“差”

# cj=int(input("请输入成绩："))
# if cj>=90:
# 	print("优秀")
# elif cj>=80:
# 	print("良好")
# elif cj>=60:
# 	print("中等")
# else:
# 	print("差")

# 3.现在有一个银行保险柜，有两道密码。
# 想拿到里面的钱必须两次输入的密码都要正确。
# 如果第一道密码都不正确，那直接把你拦在外面；
# 如果第一道密码输入正确，才能有权输入第二道密码。
# 只有当第二道密码也输入正确，才能拿到钱！
# (两道密码自己设)(嵌套if)
# m1=987726
# m2=231214
# a=str(input("请输入第一密码："))
# if a=="987726":
# 	print("密码正确！")
# 	b=str(input("请输入第二密码："))
# 	if b=="031214":
# 		print("密码正确")
# 		print("请下方拿钱")
# 	else:
# 		print("密码错误")
# if a!="987726":
# 	print("密码错误")

# 4.开发一个计算器，用户输入第一个数、加减乘除、第二个数，控制台显示计算结果。
# n1=int(input("请输入第一个数："))
# n2=int(input("请选择计算类型(1=加法,2=减法,3=乘法,4=除法):"))
# n3=int(input("请输入第二个数："))
# if n2==1:
# 	print(n1+n3)
# elif n2==2:
# 	print(n1-n3)
# elif n2==3:
# 	print(n1*n3)
# elif n2==4:
# 	print(n1/n3)
# else:
# 	print("错误命令")
# input("点击enter键退出！")

# 案例1：
# 为一家超市开发一个简易的收银系统(以3-5种商品为例): 
# 使用变量保存：商品编号 商品价格 商品名字

# 1.提示用户输入商品编号和数量,然后显示总价多少钱。
# 2.提示用户输入付款金额,然后显示找零金额。
# a={"名称":"笔记本","价格":6,"编号":1}
# b={"名称":"茅台","价格":150,"编号":2}
# c={"名称":"洗衣液","价格":28,"编号":3}

# nm1=int(input("请输入商品编号："))
# nm2=int(input("请输入购买数量："))
# if nm1==1:
# 	print(int(a["价格"])*nm2)
# 	nm3=int(input("请输入付款金额："))
# 	print(nm3-int(a["价格"])*nm2)
# elif nm1==2:
# 	print(int(b["价格"])*nm2)
# 	nm3=int(input("请输入付款金额："))
# 	print(nm3-int(b["价格"])*nm2)
# elif nm1==3:
# 	print(int(c["价格"])*nm2)
# 	nm3=int(input("请输入付款金额："))
# 	print("找零金额",nm3-int(c["价格"])*nm2)
# else:
# 	print("无此编号")


# 案例2：
# 帮一家快递点开发一个快递价格计算器,业务如下:

# 提示用户输入:1.重量; 2.地点编号

# 快递费算法:
# 首重:3公斤   
# 3公斤以内:    东三省/宁夏/青海/海南 12元   新疆/西藏:20元 
#  港澳台/国外:不接受寄件   其他:10元
# 超过3公斤部分:东三省/宁夏/青海/海南 每公斤10元  
#  新疆/西藏:每公斤20元   港澳台/国外:联系总公司   其他:每公斤5元

# 用户输入重量和地点编号后显示快递费金额。

# a=int(input("请输入快递重量(公斤)："))
# b=input("请输入快递的地点编号：")
# if a<=3:
# 	if b=="东三省" or "宁夏" or "青海" or "海南":
# 		print(12)
# 	elif b=="新疆" or "西藏":
# 		print(20)
# 	elif b=="港澳台" or "国外":
# 		print("抱歉,不接受")
# 	else:
# 		print(10)
# if a>3:
# 	if b=="东三省" or "宁夏" or "青海" or "海南":
# 		print(12+(a-3)*10)
# 	elif b=="新疆" or "西藏":
# 		print(20+(a-3)*20)
# 	elif b=="港澳台" or "国外":
# 		print("联系总公司")
# 	else:
# 		print(10+(a-3)*5)

# 循环结构
# for 变量 in 序列：
# for x in range(1,11,3):
# 	print("第",x,"次 你是猪")

# 容器遍历
# 1.列表
# name=["李志豪","宋雪颖","潘奇","潘鑫"]
# for x in name:
# 	# print(name[1],name[0])
# 	print(x)
# 2.元组
# num=(87,89,37,57,78,99)
# for y in range(0,len(num)):

# 	print(num[y])

# for a in range(0,len(num)):  #构建索引
# 	print(a)
# b=0
# for a in num:
# 	b=b+a
# print(b/len(num))	   #求平均值

# 3.字典
# dic={"name":"李志豪","age":"19","hobby":"basketball"}
# for z in dic:
# 	print(z,":",dic[z])

# 4.集合
# 和字典基本一致

# 最大值最小值问题

# scores=[67,78,56,89,76,79,98,45,65,76]

# 最高分数
# maxScore=scores[0]
# for score in scores:
# 	if score>maxScore:
# 		maxScore=score #将更大值更新为最大值
# print(maxScore)


# 最低分数
# minScore=scores[0]
# for score in scores:
# 	if score<minScore:
# 		minScore=score #将更小值更新为最小值
# print(minScore)


# 1.用户输入任意10个数，for循环求他们的平均值；
# b=0

# for x in range(1,11):

# 	a=int(input("请输入分别输入第"+str(x)+"个数字:")) #input连接用+和str()
# 	b=b+a
# print("十个数字的平均数为：",end="")
# print(b/10)

# 2 .一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8844米）？
# a=0.08
# c=0

# while a<8844000:
# 	a=a*2

# 	c=c+1
# print(c)
# print(a)
# 3.鸡兔同笼问题：今有鸡兔同笼，上有三十五个头，下有九十四足，问鸡兔各几只？

# for j in range(36):
# 	t = 35-j
# 	m = 2*t + 4*j
# 	if m == 94:
# 		print(t, j)

# 4.我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，题意是这样的：
#    5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。现在用100文钱买100只鸡，
#    那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。

# for g in range(0,21):
# 	for m in range(0,34):
# 		for c in range(0,100,3):
# 			if g+m+c==100 and 5*g+3*m+c/3==100:  #三次循环不推荐
# 				print(g,m,c)


# for g in range(0,21):
# 	for m in range(0,34):
# 		c=100-(g+m)
# 		if g+m+c==100 and 5*g+3*m+c/3==100:
# 			print(g,m,c)
# a = [12, 34, 45, 57, 78, 89, 98]
# for x in range(1, len(a)):
#     for y in range(0, len(a)-1):  #冒泡排序
#         if a[x] > a[y]:
#             c = a[x]
#             a[x] = a[y]
#             a[y] = c
# #             print(a)

#  函数
# def fun():
#     print("hello world!")
#     a = "hello Li"
#     print(a)
#     return "hello"
# fun()
