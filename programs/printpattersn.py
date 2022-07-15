for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()

for i in range(6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(5):
    for k in range(i):
        print(" ",end=" ")
    for j in range(5-i):
        print("*",end=" ")
    print()

numbers=[1,2,3,4,5,6]
for i in range(len(numbers)):
    for j in range(i):
        print(numbers[j],end=" ")
    print()

alphabets=['A','B','C','D','E','F']
for i in range(len(alphabets)):
    for j in range(i):
        print(alphabets[j],end=" ")
    print()

lists=[['A'],['B','C'],['D','E','F'],['G','H','I','J'],['K','L','M','N','O'],
       ['P','Q','R','S','T','U'],['U','U','V','W','X','Y','Z']]
for i in range(len(lists)):
    for j in range(len(lists)):
        try:
            print(lists[i][j],end=" ")
        except Exception as e:
            pass
    print()


for i in range(5):
    for j in range(5-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()


for i in range(5):
    for k in range(i):
        print(end=" ")
    for j in range(5-i):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(5-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for j in range(5 - i):
        print("*", end=" ")
    print()

for i in range(10):
    for j in range(10-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,10):
    for k in range(i):
        print(end=" ")
    for j in range(10-i):
        print("*", end=" ")
    print()


