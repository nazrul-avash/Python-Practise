#This program consists of the solutions of 100 programming problems found in github.
#Github Link: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
import pprint
#problem -1
def problem001():
	for i in range(2000,3201):
		if i%7 == 0 and i % 5 != 0:
			print(i , end=",")
#problem -2
def problem002(num):
	if num == 0:
		return 1
	else:
		return num * problem002(num - 1)	
#problem -3		
def problem003(num):
	values = {}
	for i in range(num+1):
		values[i] = i*i
	pprint.pprint(values)	#pprint module is used to represent dictionary keys and values in a more friendly way
#problem - 4	
def problem004():
	values = input()
	val = values.split(",")
	tup = tuple(val)
	pprint.pprint(val)
	pprint.pprint(tup)
#problem - 5	
class problem005:
	def __init__(self):
		self.s = ""
	def get_string(self):
		self.s = input()
	def print_string(self):
		print(self.s)
#problem - 6:
def problem006():
	c = 50
	h = 30
	d = input()
	dList = d.split(",")
	print(dList)
problem006()		
