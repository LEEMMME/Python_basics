# 大宝的超市开业了，为了更好的管理商品信息，准备开发一个商品管理系统。
# 系统需要用户先登录，再进行操作，其中包含以下功能菜单:
#
# 1.显示商品列
# 2.增加商品信息
# 3.删除商品
# 4.设置商品折扣
# 5.修改商品信息
# 6.退出
#
# a.	使用列表嵌套字典的方式保存用户数据（包含用户名，密码，姓名）；
# b.	使用列表嵌套字典的方式保存商品数据（包含编号，名称，价格，折扣）；
# c.	编写用户登录的函数，返回登录结果；
# d.	循环提示菜单，业务完毕时返回主菜单，退出时回到登陆页面；
# e.	将功能菜单中的业务功能各自编写到函数中；
# f.	用户选择不同业务编号时，调用已经写好的各种函数。

#       1.用户信息
data1 = {"user name": "可爱的飞猪", "mima": "987726", "name": "巴克利"}
data2 = {"user name": "萌神小学生", "mima": "774125", "name": "斯蒂芬"}
data3 = {"user name": "G6佛祖汤神", "mima": "897765", "name": "汤普森"}
data4 = {"user name": "治愈笑容嘴哥", "mima": "998788", "name": "维金斯"}
data5 = {"user name": "篮板痴汉鲁大爷", "mima": "443567", "name": "鲁尼"}
list0 = [data1, data2, data3, data4, data5]

#       2.商品列表清单
commodity1 = {"number": "001", "com name": "篮球", "price": 125, "discount": 0.8}
commodity2 = {"number": "002", "com name": "冰丝袖套", "price": 65, "discount": 0.9}
commodity3 = {"number": "003", "com name": "库里9（球鞋）", "price": 1325, "discount": 0.9}
commodity4 = {"number": "004", "com name": "篮球袜（6只装）", "price": 85, "discount": 0.95}
commodity5 = {"number": "005", "com name": "勇士球衣", "price": 130, "discount": 0.85}
allproduct = [commodity1, commodity2, commodity3, commodity4, commodity5]


#       3.登陆系统
def login():
    num = "失败"
    while 1 == 1:
        a = input("请输入账户名：")
        b = input("请输入密码：")
        for x in list0:
            if a == x["user name"] and b == x["mima"]:
                num = "成功"
                print("欢迎，", x["name"])
                break
        if num == "失败":
            print("账户名或密码错误，登陆失败！")
            continue
        else:
            break
    return num


#       4.显示商品列表
def commodity():
    print("-编号----名称----价格----折扣-")
    for y in allproduct:
        print(y["number"], "----", y["com name"], "----", y["price"], "----", y["discount"])
    print("--------------------------------------")


#       5.增添商品信息
def addproduct():
    lista = []
    for product in allproduct:
        lista.append(int(product["number"]))
    newnum = str(max(lista) + 1)
    wname = input("请输入添加商品的名字：")
    wprice = int(input("请输入添加商品的价格："))
    wdiscount = float(input("请输入添加商品的折扣："))
    newproduct = {"number": newnum, "com name": wname, "price": wprice, "discount": wdiscount}
    allproduct.append(newproduct)
    commodity()


#       6.删除商品信息
def delproduct():
    while 1 == 1:
        num = 0
        sun = int(input("请输入删除商品的编号："))
        for product in allproduct:
            if sun == product["number"]:
                num = 1
                allproduct.remove(product)
                break
        if num == 0:  # 编号输入错误
            print("没有此商品编号！")
            choose = int(input("退出请按1，继续输入请按2！"))
            if choose == 1:
                break
            else:
                continue
        else:  # 编号正确
            commodity()
            break


#       7.设置商品折扣
def setdiscount():
    while 1 == 1:
        num = 0
        newnumber = int(input("请输入要设置折扣的商品的编号："))
        for number in allproduct:
            if number["number"] == newnumber:
                newdiscount = float(input("请输入该商品设置的折扣（0.1~1）"))
                number["discount"] = newdiscount
                print("---商品", number["名称"], "折扣已设置成功，", newnumber * 10, "折！")
                num = 1
                break
        if num == 0:
            print("没有此商品编号：")
            choose = int(input("退出请按1，继续输入请按2！"))
            if choose == 1:
                break
            else:
                continue
        else:
            commodity()
            break


#       8.修改商品价格信息
def setprice():
    while 1 == 1:
        num = 0
        newnumber = int(input("请输入要修改价格的商品的编号："))
        for product in allproduct:
            if product["number"] == newnumber:
                newprice = float(input("请输入该商品设置的价格："))
                product["price"] = newprice
                print("---商品", product["名称"], "价格已设置成功，", newprice, "元！")
                num = 1
                break
        if num == 0:
            print("没有该商品编号！")
            choose = int(input("退出请按1，继续输入请按2！"))
            if choose == 1:
                break
            else:
                continue
        else:
            commodity()
            break


#       6.根据价格排序显示商品列表
def sort():
    choose = int(input("请选择排序方法（1.升序 2.降序）："))
    sortlist = []
    for product in allproduct:
        sortlist.append(product["price"])
    sortlist = list(set(sortlist))
    print("-编号----名称----价格----折扣-")
    if choose == 1:
        nlist = sorted(sortlist)
        for price in nlist:
            for product in allproduct:
                if price == product["price"]:
                    print(product["number"], "-----", product["com name"], "-----", str(product["price"]), "-----",
                          str(product["discount"]))
    else:
        nlist = sorted(sortlist, reverse=True)
        for price in nlist:
            for product in allproduct:
                if price == product["price"]:
                    print(product["number"], "-----", product["com name"], "-----", str(product["price"]), "-----",
                          str(product["discount"]))


#       7.显示主菜单，调用已经写好的业务函数
while 1 == 1:
    result = login()
    if result == "成功":
        if 1 == 1:
            while 1 == 1:
                print("---------------主菜单--------------")
                print("-----", "1.显示商品列表")
                print("-----", "2.增添商品信息")
                print("-----", "3.删除商品信息")
                print("-----", "4.设置商品折扣")
                print("-----", "5.修改商品信息")
                print("-----", "6.根据价格排序商品")
                print("-----", "7.退出")
                choice = int(input("请选择业务编号（输入1-6）："))
                if choice == 1:
                    commodity()
                elif choice == 2:
                    addproduct()
                elif choice == 3:
                    delproduct()
                elif choice == 4:
                    setdiscount()
                elif choice == 5:
                    setprice()
                elif choice == 6:
                    sort()
                elif choice == 7:
                    m = input("请按enter键退出！")
                    break
                else:
                    print("没有该业务编号！")
                    continue
