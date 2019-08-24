tableData = [["apples","oranges","cherry"],["lemon", "pine","mahagony"],["Tiger"," Lion", "Hippopotamus"]]
for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        temp = tableData[j][i] 
        print(temp.rjust(10), end= " ")
    print()

