 #function for calculating string length manually:
def calLength(line):
    if line == "":
        return 0
    else:
        return 1 + calLength(line[1:])

#Function to print as required in the assignment:  
def printMisfitAssignment(words):
    length = 0
    for i in things:
        print(" "*(length) + i)
        if calLength(i) > 0:
            length += calLength(i)-1
    
things = ["Wellcome", "to", "misfit"]
printMisfitAssignment(things)
