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
def list_comp():
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())
	finalList = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) !=n ]
	print(finalList)
def secondMaximum():
    n = int(input())
    arr = set(map(int, input().split()))
    li = list(arr)
    li.sort()
    print(li[-2])
def nested_list():
    mainLi=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        subLi= []
        subLi.append(name)
        subLi.append(score)
        mainLi.append(subLi)
    mainLi.sort(key = operator.itemgetter(1))
    lowest = mainLi[0][1]
    mainLi = [seed for seed in mainLi if seed[1]!= lowest]
    lowest = mainLi[0][1]
    tempLi = [seed for seed in mainLi if seed[1]== lowest]
    fLi = [i[0] for i in tempLi]
    fLi.sort()
    print("\n".join(fLi))	
nested_list()