# Set is an unordered collection of values of different datatypes
# Set is a collection of unique values
# # like integer,float,string,boolean datatypes
# Set does not follow Indexed and not ordered
# Set can not have duplicates values
# Set is dynamic in nature it can grow/shrink in size
# Set don't follow sequence

ektaset={1,2,"EktaMehta",False}
print(ektaset)

mehtaset={98,2,9,31,3}
print(mehtaset)


mehtaset={98,2,9,31,3,3,98}
print(mehtaset)

ektaset.add(222)
print(ektaset)

mehtaset.pop()
print(mehtaset)

mehtaset.remove(31)
print(mehtaset)

mehtaset.discard(38)
print(mehtaset)
#
# mehtaset.discard(3)
# print(mehtaset)
#
# print(len((ektaset)))
#
# mehtaset.clear()
# print(mehtaset)
#
# ektacopy=ektaset.copy()
# print(ektacopy)
#
# set1=set([3,"Chakrdhar",True])
# print(set1)
# set2=set((1,"EktaMehta",78,True))
# print(set2)

ektasetsss={1,2,"EktaMehta",False}
print(ektasetsss)
for val in ektasetsss:
    print(val)