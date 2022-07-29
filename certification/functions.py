def display(day, month, year):
    print("Date: ", day)
    print("Month: ", month)
    print("Year: ", year)


def init():
    display(23, 7, 2022)


init()


def d_display(day, month, year=2019):
    print("Date: " + str(day))
    print("Month: ", str(month))
    print("Year: ", str(year))


d_display(23, 15)
d_display(23, 14, 2023)
d_display(year=2024, day=24, month=12)


def display_data(*data):
    for d in data:
        print(d)


display_data("Allen", 6.4, 34, True)


def sumo(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total Sum : ", total)


sumo(10, 20)
sumo(10, 50, 1000, 34, 76, 85)


def fun():
    return 10, 20


a, b = fun()
print(a, b)


def equal(x, y):
    return x == y


flag = equal(10, 10)
print(flag)
flag = equal(10, 5)
print(flag)

data=(10,20,30)
if 60 in data:
    print('yes')
else:
    print('ON')
