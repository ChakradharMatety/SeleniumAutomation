# Python – List Comprehension
# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.
# Syntax of  List Comprehension
# newList = [ expression(element) for element in oldList if condition ]

# Using list comprehension to iterate through loop
mylist=[1,2,3,4,5,6,7,8,9,10]
print([element for element in mylist])

# Even list using list comprehension using if
values=[element for element in range(11) if element%2==0]
print(values)

# Display square of numbers from 1 to 10 using List Comprehension.
squares=[n**2 for n in range(21)]
print(squares)

# Python List Comprehension Using If-else
val=["Even Numbers" if i%2==0 else "odd Number" for i in range(10)]
print(val)

# Using list comprehension to iterate through loop
str='Geeks 4 Geeks!'
strlist=[ch for ch in str]
print(strlist)
str_list=[ch for ch in 'Geeks 4 Geeks!']
print(str_list)

# Nested list comprehension
matrix=[[j for j in range(5)]for i in range(3)]
print(matrix)

# using list comprehension to print table of 10
table=[10*i for i in range(1,6)]
print(table)

# Nested IF with List Comprehension
values=[num for num in range(100) if num%5==0 if num%10==0]
print(values)

# Reverse each string in a tuple.
tuples=("Book","six","Four")
list=[val[::-1] for val in tuples]
print(list)

# Set Comprehension
my_set={i for i in range(11) if i%2==0}
print(my_set)

squares={n**2 for n in range(21)}
print(squares)