in_str = "banana"
length = len(in_str)
count = 0
for i in range(length):
	n = length - i
	for j in range(n):
		print(in_str[i:length-j])
		count += 1
	print("-----------------------------")	
print(count)