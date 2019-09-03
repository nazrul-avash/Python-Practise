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
def execute_command(command,*args):
    
    if command == "insert":
        print("ye")
        li.insert(args[0],args[1])
    elif command == "print":
        print(li)
    elif command == "append":
        li.append(args[0])
    elif command == "pop":
        li.pop()
    elif command == "remove":
        li.remove(args[0])
    elif command == "reverse":
        li.reverse()
    elif command == "sort":
        li.sort()           

li = []
num = int(input())
for i in range(num):
    sr = input().split()
    command = sr[0]
    if len(sr) is 3:
        execute_command(command,int(sr[1]),int(sr[2]))
    elif len(sr) is 2:
        execute_command(command,int(sr[1]))
    else:
        execute_command(command)    
                
n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))

def swap_case(s):
    temp =""
    for x in s:
        if x.isupper():
            temp += x.lower()
        else:
            temp += x.upper()
    return temp
def split_and_join(line):
    # write your code here
    new_str = line.split()
    return "-".join(x for x in new_str)
def string_validators():
    s = input()
    li = [0,0,0,0,0]
    for x in s:
        if x.isalnum():
            li[0] += 1
        if x.isalpha():
            li[1] += 1

        if x.isdigit():
            li[2] += 1

        if x.islower():
            li[3] += 1

        if x.isupper():
            li[4] += 1        
    for x in li:
        if x > 0:
            print("True")
        else:
            print("False")
def minion_game(in_str):
    
    kevin,stuart = 0,0
    length = len(in_str)
    for x in range(length):
        if in_str[x] in "AEIOU":
            kevin += length - x
        else:
            stuart += length -x
    if kevin > stuart:
        print("Kevin"+ " "+ str(kevin))
    elif kevin < stuart:
        print("Stuart"+ " "+ str(stuart))
    else:
        print("Draw")
def wrap(in_str, seed):

    li = []
    for x in range(0,len(in_str),seed):
        li.append(in_str[x:x+seed])
    in_str2 = "\n".join(li)
    return in_str2
def time_delta(first_str, second_str):

    dt_first = datetime.datetime.strptime(first_str,"%a %d %b %Y %H:%M:%S %z")
    dt_second = datetime.datetime.strptime(second_str,"%a %d %b %Y %H:%M:%S %z")
    delt = abs(dt_first - dt_second).total_seconds()
    delt = int(delt)
    return str(delt)
def find_weekday():
    in_str = input()
    dt = datetime.datetime.strptime(in_str,"%m %d %Y")
    date_ob = datetime.datetime.date(dt)
    print(datetime.datetime.strftime(dt,"%A").upper())
def solve(in_str):
    return " ".join(i.capitalize() for i in in_str.split(" "))
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score +=1
    return score
def print_formatted(num):    
    pad = len("{0:b}".format(num))
    pad = str(pad)
    for x in range(1,num+1):
        st ="{0:"+pad+"d} {0:"+pad+"o} {0:"+pad+"X} {0:"+pad+"b}"
        print(st.format(x))    

