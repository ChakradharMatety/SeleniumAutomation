# Reverse words in a string
str =" geeks quiz practice code"
# listStr=str.split()[::-1]
# for words in listStr:
#     print(words,end=" ")
# print(len(listStr))
# for words in listStr:
#     print(words)
#
# for i in range(len(listStr)):
#     print(i)
#
# for i in range(len(listStr)):
#     print(listStr[len(listStr)-1-i],end=" ")


# Ways to remove i’th character from string in Python
# strs="I Love Python"
# s=strs.replace('P','')
# print(s)


# Python | Check if a Substring is Present in a Given String
strs="I Love Python"
Sub_String='Python'
if strs.find(Sub_String)==-1:
    print("no")
else:
    print('Yes')

if 'Python' in strs:
    print('YES')
else:
    print('No')

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










