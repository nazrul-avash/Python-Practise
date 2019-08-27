def compressed_string(line):
	temp = line[0]
	count = 0
	compressed =""
	for x in range(len(line)):
		if temp == line[x]:
			count +=1
		else:
			compressed += temp+ str(count)
			count = 1
			temp = line[x]
	compressed +=temp+str(count)		
	return compressed
def find_prefix(names,prefix):
	prefix_list = [x for x in names if x.startswith(prefix)]
	return prefix_list
print(compressed_string("aaaabcccccdddd"))