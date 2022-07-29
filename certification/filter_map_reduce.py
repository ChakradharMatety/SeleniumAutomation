from functools import reduce
import logging
# The filter() method filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.
# filter(function, sequence)
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
# mentioned in the sequence passed along.This function is defined in “functools” module.
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Educator", "", "", "Venezuela"]

print(list(filter(None, countries)))

nums = [3, 2, 7, 8, 4, 2, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
doubles = list(map(lambda x: x * 2, evens))
print(doubles)
total=reduce(lambda y, z: y + z, doubles)
print(total)

