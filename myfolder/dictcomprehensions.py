# Python Dictionary Comprehension
# A dictionary comprehension takes the form {key: value for (key, value) in iterable}

# Python code using dictionary comprehension
keys=['a','b','c','d','e']
values=[1,2,3,4,5]

mydict={k:v for(k,v) in zip(keys,values)}
print(mydict)

# Display square of numbers using list comprehensions
my_dict={i:i**2 for i in range(11)}
print(my_dict)

# Display cubes of numbers using list comprehensions using if
my_dicties={x:x**3 for x in range(11) if x%2==0}
print(my_dicties)


test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
dicts={}
for key in test_str.split():
    counter=test_str.count(key)
    dicts.__setitem__(key, counter)
print(dicts)

my_dictwords={key:test_str.count(key) for key in test_str.split()}
print(my_dictwords)

str = 'ABBCDDDD'
new_dicts={}
for key in str:
    counter=str.count(key)
    new_dicts.__setitem__(key, counter)
print(new_dicts)

mydict={key:str.count(key) for key in str}
print(mydict)