# int,float,str,bool,complex datatypes are immutable -- Non Changeable
# once object created we cannot change its content
# if we try to make changes it will create new object with those changes
# # int
# # float
# # bool
# # str
# # list
# # tuple
# # set
# # dict
# # range
# # None
# # ----------
# # complex
# # bytes
# # bytearray
# # frozenset
# # Integer
# # ===========
# x=10
# # whole numbers|integral values
# # print(type(x))
# # print(id(x))
# # a=0B11
# # print(a)
# # In Python every thing is treated as object no primitive data types
# # Dynamically Typed Programing Language -Python,Javascript
# # int x=10
# # Statically typed programing language - Java
# #
# # Python predefined inbuilt functions
# # type()
# # id()
# # print()
# # Float
# # =========
# # weight = 76.90
# # Scientific notation|Exponential form
# # print(type(weight))
# # print(id(weight))
# # print(weight)
# # x=1.2E3
# # print(type(x))
# # print(id(x))
# # print(x)
# # y=+2e3
# # print(type(y))
# # print(y)
# # x=10+20j
# # print(type(x))
# # print(x)
# # Bool
# # =========
# # x=True
# # y=False
# # print(type(x))
# # print(type(y))
# # print(x)
# # print(y)
# # a=10
# # b=20
# # c=a>b
# # print(type(c))
# # print(c)
# # # True is 1 and False is 0
# # print(True+True)
# # print(True+False)
# # print(False+False)
# # print(11+True)
# # String
# # ==========
# # s='chakri'
# # s="chakri"
# # print(type(s))
# # "triple quote is  for multi line string literal"
# # strip='''chakri's
# #                "Hero"'''
# # print(strip)
# # strips="""chakri's
# #                Hero
# #                   today"""
# # print(strips)
# # singlequotes="Chakra is 'nice guy'"
# # singlequotes='Chakra is "nice guy"'
# # print(singlequotes)
# # indexing
# # s='durga'
# # print(s[0])
# # print(s[-1])
# # print(s[10])
# # slicing
# # s='abcdefghij'
# # print(s[0:])
# # print(s[:-1])
# # print(s[2:6])
# # print(s[:6])
# # print(s[-6:-1])
# # print(s[1000:2000])
# # print(s[-1:])
# # print(s[0:9:2])
# # print(s[-1:-9:-2])
# # print(s[0:9:0]) # Value Error
#
# # Type Casting
# # Type Coersion
# int()
# float()
# complex()
# bool()
# str()
# print(int(123.456))
# print(int(True))
# print(int(False))
# print(int('123'))
# # print(int('123.0'))
# print(int(1+2j))
# print(complex(10))
# print(complex(10.5))
# print(complex(True))
# print(complex(10,20))
# name=input('Enter your Name : ')
# married=bool(input('Are you married[True|False] : '))
# married=eval(input('Are you married[True|False] : '))
# print('Name:',name)
# print('Married:',married)
# print(bool(0))
# print(bool(1))
# print(bool(-10))
# print(bool(10.123))
# print(bool(10+20j))
# print(bool(0+0j))
# print(bool(0.0))
# print(bool(''))
# print(bool(' '))
# print(bool('Hello'))
# print(bool(None))
# s=student()
# bool(s) passing Object
# print(bool(True))
# print(bool(False))

# x=10
# y=x
# print(x,y)
# x=x+1
# print(x,y)

# s1='durga'
# s2=s1
# print(s1,s2)
# s1=s1+' software'
# print(s1)

# list is Mutable
# l1=[10,20,30,40]
# l2=l1
# print(l1,l2)
# l2.append(50)
# print(l2)

# a=10
# b=100000000000000
# c=10
# print(id(a),id(b),id(c))

# li=[10,20,30]
# print(type(li))
# tup=(10,20,30)
# print(type(tup))
# s={10,20,30}
# print(type(s))
# di={102:'ravi',103:'durga'}
# print(type(di))

# Heterogeneous
# list order is preserved
# it is mutable
# duplicates are allowed
# indexing and slicing is allowed
# dynamic values are allowed
# li=[]
# li.append(11)
# li.append(12.5)
# li.append(True)
# li.append('Capgemini')
# li.append([(102,'Chakra')])
# li.append([100.101,102,104])
# print(li)
# print(li[0])
# print(li[-1])
# print(li[2:])
# print(li[1:5])
# li[0]=22
# print(li)

# tuple()
# ------
# Heterogeneous
# list order is preserved
# it is immutable
# duplicates are allowed
# indexing and slicing is allowed
# allowed values are Fixed

# set{}
# order is not preserved
# duplicates are not allowed
# it is mutable
# s={10,20,True,10.5,'Chakra'}
# print(type(s))
# print(s)
# s.add('cv')
# print(s)
# s.add(10)
# print(s)

# range data type
# it is immutable does not support type assignment
# r= range(10)
# for i in range(1,50,2):
#     print(i)
#
# for i in range(10):
#     print(i)

# li=list(range(1,10))
# print(li)
# s=set(range(1,10))
# print(s)
# t=tuple(range(1,10))
# print(t)
# di=dict()
# di[1]={'chakri':'hero'}
# print(di[1].values())
# print(di[1].keys())
# print(di[1])
# print(10/2);
# print(10.0/2);
# print(10//2);
# print(10.0//2);
# print(10/3);
# print(10.0/3);
# print(10//3);
# print(10.0//3);
# print(4%2);
# print(10*2)
# print(10**2)
# print(3**2)
# print(10+20)
# print('10'+'20')
# print('10'+str(20))
# print('10'*2)
# print('AB'*5)
# print(5*'CD')
# print(10*'$')
for i in range(10):
    print(i*'*')

for i in range(10):
    print((10-i) * '*')
#
for i in range(10):
    print((10-i)*' ',end="")
    print(i* '*')
for i in range(10):
    print(i * ' ',end='')
    print((10-i)*'*')


# #Print Triangle
# for i in range(10):
#     print((10 - i) * ' ', end=" ")
#     print(i * '* ')

#Print reverse Triangle
# for i in range(10):
#         print(i * ' ', end=" ")
#         print((10 - i) * ' *')

# for i in range(5):
#     print((5 - i) * ' ', end=" ")
#     print(i * '* ')
# for i in range(5):
#     if i!=0:
#         print(i * ' ', end=" ")
#         print((5 - i - 1) * ' *')

# for i in range(10):
#     print(i,end=" ")

# Relation Operators:
# <,>,<=,>=

# print('durga'<'ravi')
# print(True>False)
# print(True<False)
# # print('abc'>10) # not supported
# print('abc'>'10')
# print(10<20<30)
# print(10<20<30>40)
# print(ord('a'))
# print(ord('A'))
# print(chr(99))
# print(chr(67))
# print('durga'<='don')
# print('durga'>='don')
# print('durga'>='durga')
# print('Durga'<'durga')

# Equality Operators
# == and != meant for content comparision
# is operator is reference(address) comparision
# print(10==20)
# print(10 is 20)
# print(10==10)
# print(10 is 10)
# print(10!=20)
# print(10 is not 20)
# print(10=='durga')
# print('durga'=='durga')
# l1=['sunny','bunny','chinny','vinny']
# l2=['sunny','bunny','chinny','vinny']
# print(l1 is l2)
# print(l1 == l2)
# print(l1 is not l2)
# print(l1!=l2)
# l1=l2
# print(l1 is l2)
# print(l1 == l2)
# print(l1 is not l2)
# print(l1!=l2)
# print(10==10 and 20==20)
# print(10==10 and 20!=20)
# print(10!=10 or 20==20)
# print(not 10==10)
# print(not 10==20)
#
# name=input("Enter Username :")
# pwd=input("Enter Pwd :")
# if name=='durga' and pwd=='king':
#     print('Valid User')
# else:
#     print('Invalid User')

# print(not 0)
# print(not 10)
# print(not '')
# print(not 'durga')
# print(not None)

# Identity Operatore
# is and is not are identity operators
# membership Operators
# in and not in are membership operators
print('r' in 'durga')
print('z' in 'durga')
li=['apple','orange','mango']
print('Banana' in li)
print('orange' in li)
print('Banana' not in li)
d={1:'A',2:'B'}
if 3 in d:
    print('available')
else:
    print('not available')

if 'A' in d.values():
    print('available')
else:
    print('not available')

# ternary operator
# a=10
# b=5
# min=a if a<b else b
# print(min)
#
# a=10
# b=5
# c=1
# min=a if a<b and a<c else b if b<c else c
# print(min)
# min =a if a<b<c else b if b<a<c else c
# print(min)
# operator precedence
# Parenthesis()
# exponential operator **
# bitwise operators,unary minus operator
# multiplication has higher predidence *,next /,%,//
# next +,-
# <<,>> shift operators
# &,^,|
# >,>=,<<=,==,!=
# is,is not
# in ,not in
#logical and,or,not
# print(10+20*3)
# result=(2*(3+4)**2-(3**3)*3)
# print(result)

# a=1
# b=2
# c=4
# d=6
# x=a+b
# y=d-c
# print(x)
# print(y)
# print(x//d)
# print(11/3)
# print(13//4)
# print(1%3)
# print(type(''))
# count=input('Enter the value : ')
# print(int(count)+1)

# name=input()
# print(name)
# a=10
# b=20
# print(a+b)
# a,b,c=10,20,30
# print(a,b,c)
# print(b)
# print(c)
# d,e,f=10.5,True,'Chakradhar'
# print(d,e,f)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))
# num1=num2=num3=0
# print(num1,num2,num3)












