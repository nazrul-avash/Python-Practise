#This explores variable scope:
def k():
    print(x)
def f():
    	
    x = 99
    def g():
        nonlocal x   
        x =43
        print(x)
    def l():
        global x
        x=100
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
f()
print("x in main: " + str(x))
k()
