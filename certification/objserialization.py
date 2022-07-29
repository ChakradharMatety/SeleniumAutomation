import pickle

f=open("pickled.txt","wb")
dict={'UserName':'Chakradhar'}
pickle.dump(dict,f)
f.close()

f=open("pickled.txt","rb")
d=pickle.load(f)
print(d)

for i in d:
    print(d[i])
f.close()