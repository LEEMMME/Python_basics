# 案例：模拟银行ATM存款取款
#
# 1.	模拟3张银行卡,1001,1002,1003,分别设置密码和余额(使用列表嵌套字典的方式)；
#
# 2.	提示用户输入银行卡和密码，遍历每张卡的信息验证是否成功；
#
#
# 3.	如果用户输入正确---提示让用户选择取款.存款还是退出,并提示余额多少.  输入错误---重新输入卡号密码；
#
# 选择取款---提示输入取款额度,如果超过余额,提示余额不足;否则,在余额上减掉相应金额；
#
# 选择存款---输入存款额度,余额加上相应额度,并提示余额多少；
#
# 选择退出---重新登录；
#
# 4.	设置3次输入错误账号密码,提示银行卡已被锁定，程序结束。
# cake1 = {"num": "1001", "mima": "1289", "yue": 77940}
# cake2 = {"num": "1002", "mima": "1456", "yue": 78452}
# cake3 = {"num": "1003", "mima": "9299", "yue": 73490}
# cakeall = [cake1, cake2, cake3]
# a = input("请输入银行卡号：")
# b = input("请输入密码：")
# for inf in cakeall:
#     if a == inf["num"] and b == inf["mima"]:
#         print("您的余额为：", inf["yue"])
#         chse1 = "存款"
#         chse2 = "取款"
#         chse3 = "退出"
#         c = input("请选择存款；取款；退出:")
#         if c == chse1:
#             l = input("请输入存款金额：")
#             print("余额为：", inf["yue"] + int(l))
#             q = input("点击enter键退出！")
#         if c == chse2:
#             m = input("请输入取款款金额：")
#             if int(m) > inf["yue"]:
#                 print("余额不足！请先进行充值。")
#             if int(m) < inf["yue"]:
#                 print("取款成功！余额为：", inf["yue"]-int(m))
#                 h = input("点击enter键退出！")
#         if c == chse3:
#             n = input("点击enter键退出!")
#     else:
#         print("密码错误请重新登陆！")
#         break

# 1.写函数，接收3个数字参数，返回最大的那个数字。
# def mma(a, b, c):
#     mn = max([a, b, c])
#     return mn
#
#
# we = mma(34, 38, 89)
# print(we)


# 2.编写一个用户登录函数（用户名密码提前设置）；
# 返回用户登录成功或者失败的结果；
# def card1():
#     a = "李志豪"
#     b = "98765"
#     c = input("请输入用户名：")
#     d = input("请输入密码：")
#     e = "登陆成功"
#     f = "登陆失败"
#     if a == c and b == d:
#         return e
#     else:
#         return f
#
#
# w = card1()
# print(w)


# 3.做一个分数统计器：
# 函数中让用户循环输入一组分数，输入结束后保存到一个列表中。
# 把平均分，最高分，最低分，及格人数，及格率返回出来（接收列表为参数）。
# def data1(list1):
#
#     a = max(list1)
#     b = min(list1)
#     i = 0
#     for x in bn:
#         if x > 60:
#             i = i +1
#     n = i
#     f = int(i) / len(list1)
#     return a, b, n, f
#
#
# bn = [23, 43, 56, 78, 89, 90, 87, 90, 94, 76]
# w, u, o, p = data1(bn)
# print(w, u, o, p)
# a = {"name": "li", "xb": "女"}
# print("字典长度：%d" % len(a))
# print("字典长度：", len(a))
# 读写文件
# a = r"D:\暂时练习文件\文本文档.txt"
# b = open(a, "r", encoding='utf-8')  # 指定编码方式 encoding='utf-8'
# c = b.read()
# b.close()


# print(c)
# user = []
# for line in open(r"D:\暂时练习文件\文本文档.txt", "r"):
#     line = str(line).encode('GBK')
#     line = line.decode('utf-8')
#     user.append(line)
# print(user)

# q = "我想去迪士尼！"
# w = open(r"D:\暂时练习文件\文本文档.txt", "a", encoding='utf-8')
# data = w.write(q)
# end = w.close()
# print(data、


