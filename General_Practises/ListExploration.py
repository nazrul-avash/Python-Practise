def findFromList(name):
    if name in fruits:
        return fruits.index(name)
    else:
        return "not here"
fruits = ["Bangee", "Dungee", "Coconut", "Jackfruit"]
name = input()
print(findFromList(name))    
