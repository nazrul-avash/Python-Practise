import datetime
age = int(input())
dt = datetime.date.today()
year = int(dt.strftime("%Y")) + (100-age)
print(year)

