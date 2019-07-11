print("number:")
boolean = True
while(boolean):
    try:
        number = int(input())
        print(number**2)
        boolean = False
    except ValueError:
        print("enter a number!")
    
