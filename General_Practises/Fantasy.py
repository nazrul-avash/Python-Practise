#a fantasy game problem from the book
def displayInventory(inventory):
    sum = 0
    print("Inventory:")
    for i,j in inventory.items():
        sum += j
        print(str(j) + "  " + i)
        print("total number of items " + str(sum))
def updateInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i] + 1

stuff= {"rope":1,"bomb":2,"torch":45}
loot = ["rope", "torch","rope"]
displayInventory(stuff)
updateInventory(stuff,loot)
displayInventory(stuff)    
        
                                     
