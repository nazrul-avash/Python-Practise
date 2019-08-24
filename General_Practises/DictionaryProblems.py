#This program consists of practise problems on python dictionary data structure.
import operator
def merge(a,b):
    datas = {}
    if len(a) == len(b):
        j = 0
        for i in a:
            datas[i] = b[j]
            j += 1           
    print(datas)
def sum():
    sum = ""
    for i in bands.values():
        sum += i
    print(sum)  
def square():
    datas = {}
    for i in range(1,16):
        datas[i] = i**2
    print(datas)
def generatePower(n):
    datas = {}
    for i in range(0,n,1):
        datas.update({n:n*n})
        n = n - 1
    print(datas)
def isPresent(item):
    if item in fruits:
        print(item + " is present in dict")
    else:
        print(item +" not present")
def concatDict(a,b):
    c ={}
    for i in (a,b):
        c.update(i)
    return c    
def addKey(datas):
    datas.update({"Kiwi" : "x"})
    print(datas)
def sortByValue(datas):
    for i in sorted(datas.items(), key = operator.itemgetter(1)):
        print(i)
   
    
    
fruits = {"apple": "z", "orange":"a","mango":"e"}
bands = {"rock": "Megadeath", "post-rock": "God is an astronaut", "Death metal" : "Disturbed"}
myDict = {'data1':100,'data2':-54,'data3':247}
list1 = list(bands.keys())
list2 = list(fruits.keys())
merge(list1,list2)
