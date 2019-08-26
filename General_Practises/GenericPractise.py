in_str = "asdagasgaf"
li = []
for x in range(0,len(in_str),4):
	li.append(in_str[x:x+4])
in_str2 = "\n".join(li)
print(in_str2)	