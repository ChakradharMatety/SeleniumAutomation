from _datetime import datetime


# datetime.now()
current_time=datetime.now()
print(current_time)
print(current_time.strftime("%y-%m-%d %H:%M:%S"))
print(current_time.hour)
print(current_time.minute)
print(current_time.month)
print(current_time.day)
print(current_time.year)