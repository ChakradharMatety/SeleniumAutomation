list=[10,20,True,"Monkey",6.9,'A']
for i in list:
    print(i)
print(len(list))
print(list[0])
for i in range(len(list)):
    print(list[i])
print(list[0:3])
print(list[-1])
list2 = [60,12.9]
list.extend(list2)
for i in list:
    print(i)
list.append(False)
print(list)
print(list.count(True))
list.remove(False)
print(list)
# Calling pop method by passing index
list2.pop(0)
print(list2)
# Calling pop method without passing index
# pop method is an example of method overloading where method name is same but difference in number of parameters passed
list.pop()
print(list2)
list4 =[90,10,60,20]
list4.sort()
print(list4)
list4.reverse()
print(list4)

