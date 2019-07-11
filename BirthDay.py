birthDays = {"Alice": "2 april", "Bob": "5 june", "Carol": "12 july"}
while True:
    print("Enter a name:")
    name = input()
    if name == "":
        break
    if name in birthDays:
        print(birthDays[name] + " is the birth day of" + name)
    else:
        print(name +" is not added")
        bDay = input()
        birthDays[name] = bDay
        print("Updated")
dates = list(birthDays.keys())
print(dates)
del dates[1]
print(birthDays)
print(dates)
