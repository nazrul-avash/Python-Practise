import datetime
first_str ="Sun 10 May 2015 13:54:36 -0700"
second_str ="Sun 10 May 2015 13:54:36 -0000"
dt_first = datetime.datetime.strptime(first_str,"%a %d %B %Y %H:%M:%S %z")
dt_second = datetime.datetime.strptime(second_str,"%a %d %B %Y %H:%M:%S %z")
print(int((dt_first - dt_second).total_seconds()))