def collatz(number):
    if(number %2 ==0):
        print(number // 2)
        return number // 2
    else:
        print(3* number +1)
        return 3* number +1
print("enter number:")
try:
    number = int(input())
    flag = 0
    while(flag != 1):
        flag = collatz(number)
        number = flag
except ValueError:
        print("enter a number.")


