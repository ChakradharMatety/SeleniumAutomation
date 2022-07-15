str="i am from india"
print(len(str))

print(str[-5:-1])
print(str.index('f'))
print(str.replace('i','E'))

counter=0
for ch in str:
    if ch=='i':
        counter+=1

print(counter)
print(str.count('f'))
print(str.upper())
print(str.lower())
print(str.title())
print(str.islower())
print(str.isupper())
print(str.split(" "))

country="Germany"
strs="i am from {}".format(country)
print(strs)

strs="i am from {} {} {}".format("Germany","Poznana","California")
print(strs)

strs="i am from {2} {0} {1}".format("Germany","Poznana","California")
print(strs)

strs="i am from {P} {C} {G}".format(G="Germany",P="Poznana",C="California")
print(strs)