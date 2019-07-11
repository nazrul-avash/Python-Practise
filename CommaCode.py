def addcomma(name):
    line= ""
    for i in range(len(name)):
        if i == len(name)-2:
            line+= name[i]+ ", and "
        elif i == len(name) -1:
            line+= name[i]
        else:
            line += name[i]+", "
    return line

spam= ["apples", "oranges", "Beet", "Eggs"]
print(addcomma(spam))
