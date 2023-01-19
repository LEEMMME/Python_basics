number = input("请给你的颜值打个分数1-10分：")

if 10 > int(number) >= 8:
	print("你以为你是王祖贤吗，脸都不要的啦")
elif 5 <= int(number) < 8:
	print("喂，你对自己还蛮自信耶！可不可以低调一点呀？")
elif 0 < int(number) < 5:
	print("嘿，你要不要这么悲观呀，世界还是很美丽的啦，出去走走嘛，你还没看完大好河山呢！")

else:
	print("请输入正确命令")

input("按下enter键退出")
