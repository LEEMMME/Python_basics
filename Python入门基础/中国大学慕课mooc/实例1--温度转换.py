a = input()
if a[0] in ['f', 'F']:
    c = (eval(a[1:])-32)/1.8
    print("C{:.2f}".format(c))
elif a[0] in ['c', 'C']:
    f = eval(a[1:])*1.8+32
    print("F{:.2f}".format(f))
else:
    print("输入格式错误")
