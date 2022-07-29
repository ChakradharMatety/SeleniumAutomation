# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)
# map() function returns a map object(which is an iterator) of the results after applying
# the given function to each item of a given iterable (list, tuple etc.)
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
# mentioned in the sequence passed along.This function is defined in “functools” module.
import functools
import itertools
import operator
from functools import reduce

(2,4,8,10)
x=list(map(lambda x:x+x,(2,4,8,10)))
print(x)

def myfunc(a, b):
  return a + b

x = list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
print(x)

y=list(map(lambda a,b:a+b,('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
print(y)

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# reduce
# initializing list
lis = [1, 3, 5, 6, 2, ]
sum=reduce(lambda a,b:a+b,lis)
print(sum)
max=reduce(lambda a,b:a if a>b else b,lis)
print(max)

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.add, ["geeks", "for", "geeks"]))

# initializing list
lis = [1, 3, 4, 10, 4]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))

# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x + y, lis))

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))