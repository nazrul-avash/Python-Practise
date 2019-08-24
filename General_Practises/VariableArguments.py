def  summation(*arg):
	print(type(arg))
	sum = 0
	for i in arg:
		sum += i
	return sum
print(summation(5,7))
print(summation(6,4,9,4))
