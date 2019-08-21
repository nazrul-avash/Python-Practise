def loops():
	n = int(input())
	for i in range(n):
		print(i*i)
def Python_if_else():
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
def is_leap(year):
    leap = False
    if year%400 ==0 or (year %4 ==0 and year % 100 != 0):
        leap = True
    return leap        
def print_function():
	n = int(input())
	s = ""
	for i in range(1,n+1):
		s += str(i) 
	print(s)
def average(array):
    values = set(array)
    res = sum(values)
    return (res/len(values))
def symmetric_differenced():
	m = int(input())
	mLine = input()
	n = int(input())
	nLine = input()
	mVal = set(mLine.split())
	nVal = set(nLine.split())
	fVal = list(mVal.symmetric_difference(nVal))
	ffVal = list(map(int,fVal))
	ffVal.sort()
	print(ffVal)
symmetric_differenced()
