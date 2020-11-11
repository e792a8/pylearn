l = []
m = {"id":0,"name":1,"fresh":2,"major":3}

def insert(args):
	global l, m
	l.append(args)

def select(args):
	global l, m
	for i in l:
		if i[m[args[0]]] == args[1]:
			for j in i:
				print(j)
			print("")

def delete(args):
	global l, m
	t = []
	for i in range(len(l)):
		if l[i][m[args[0]]] == args[1]:
			t.insert(0,i)
	for i in t:
		l.pop(i)

def modify(args):
	global l, m
	for i in range(len(l)):
		if l[i][m[args[0]]] == args[1]:
			l[i][m[args[2]]] = args[3]

def sort(key):
	global l
	l.sort(lambda x: x[m[key[0]]])

def help(args):
	print("命令列表：")
	print("insert <id> <name> <fresh> <major>")
	print("\t添加一位学生的信息。")
	print("select <key> <value>")
	print("\t查询符合 key = value 条件的学生。")
	print("delete <key> <value>")
	print("\t删除符合 key = value 条件的学生。")
	print("modify <key> <value> <key2> <value2>")
	print("\t将符合 key = value 条件学生的 key2 修改为 value2。")
	print("sort <key>")
	print("\t将学生列表以 key 字段进行排序。")
	print("quit")
	print("\t退出系统，并将学生信息表保存到文件。")

print(" i i i欢迎使用全旧一代的学生信息管理系统! ! ! ")
print("使用‘help’命令获取帮助。")

while True:
	cmd = input("> ").split()
	if cmd[0]=="quit":
		break
	{
		"insert":insert,
		"select":select,
		"delete":delete,
		"modify":modify,
		"sort":sort,
		"help":help
	}[cmd[0]](cmd[1:])

with open("data.txt","w",encoding="utf-8") as f:
	for i in l:
		for j in i:
			f.write(j+'\n')
		f.write('\n')