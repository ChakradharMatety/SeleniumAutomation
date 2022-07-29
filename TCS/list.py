# List is a collection of values of different datatypes
# like integer,float,string,boolean datatypes
# List is Indexed and ordered
# List can have duplicates values
# List is dynamic in nature it can grow/shrink in size
# List is mutable like append,insert,pop

list1=[10,50,60,70,70]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

print(list1.count(70))

print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])

print(list1[0:])
print(list1[0:3])
print(list1[1:4])

list1.append("chakradhar")
print(list1)
print("-----------")
list1.remove(50)
print(list1)

list1[0]=999
print(list1)


#
# list1.pop(2)list1.insert(2,666)
# print(list1)
# print(list1)
#
# # print(list1[5])
# # print(list1)
# # print(type(list1))
# #
list2=["Mukesh",10,12.5,True]
list1.extend(list2)
print(list1)
#
# list3="Monkey"
# list1.extend(list3)
# print(list1)
#
list4=[6,99,12,56,32,3,1]
list4.sort()
print(list4)
list4.reverse()
print(list4)
#
mylist=[10,20,30,["Chakra","Ekta","Mehta"]]
print(mylist)
print(mylist[3][1:])
#
# # print(list2)
# # print(type(list2))
# #
# # print(len(list2))
# #
# # list3 = list1+list2
# # print(list3)
# # print(len(list3))
#
#
# for val in list1:
#     print(val)

