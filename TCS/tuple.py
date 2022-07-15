# Tuple is a collection of items
# Tuple is ordered and Indexed
# Tuple is Immutable(Cannot change values assigned in tuple) & List is Mutable
mytuple=(11, "Robot", True, 99,99,99,22,22,"python")
print(type(mytuple))
print(mytuple)
print(mytuple[1])
print(mytuple[-1])
print(mytuple.count(99))
print(mytuple.index(22))
print(mytuple[1:8])
myset=set(mytuple)
print(myset)
mytuple[10]="Hello"
print(mytuple)
# 'tuple' object does not support item assignment which is immutable

