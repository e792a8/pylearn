with open("data.txt","w",encoding="utf-8") as f:
	while True:
		id = input("你的学号：")
		while not len(id) == 9:
			id = input("学号应该为9位数，请重新输入：")
		name = input("你的姓名：")
		current = input("是否为应届生：")
		major = input("你的专业名称：")

		print("以下是你填写的信息。")
		print("学号：",id)
		print("姓名：",name)
		print("是否应届：",current)
		print("专业名称：",major)
		f.write(id+'\n'+name+'\n'+current+'\n'+major+'\n\n')
		if not "y"==input("是否继续？（y继续，n结束）"):
			break