# See output values are not displayed in order / sequence not followed
myset1={96,69,180.0,"Chakradhar",True}
print("Myset1: "+str(myset1))
print(len(myset1))

# Duplicate values are not allowed see output only unique values are displayed
myset2={96,69,180.0,"Chakradhar",True,True}
print("Myset2: "+str(myset2))

myset1.add(64)
print("Myset1: "+str(myset1))

# i am adding duplicate value 96 into set see output it is not accepting val 96 into set
myset1.add(96)
print("Adding Duplicate value Myset1: "+str(myset1))

myset1.remove(True)
print("Using Remove Method :"+str(myset1))

# pop deletes random value from set
myset1.pop()
print("Using pop Method :"+str(myset1))

# discard method will not throw error if val not found in set
myset1.discard(64)
print("Using discard Method : "+str(myset1))

# remove method will throw error if val not found in the set
myset1.remove(False)
print(myset1)
