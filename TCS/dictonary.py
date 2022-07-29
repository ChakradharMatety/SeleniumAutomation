# dict={"Hero":"Chakri","Heroin":"Ekta"}
# print(dict)
# print(type(dict))
# print(dict["Heroin"])
# print(dict.get("Hero"))
# dictnew={"Hero":"Chakri","Heroin":["Ekta","Shivani"]}
# print(dictnew["Heroin"])
# print(dictnew["Heroin"][0])
dictinsidedict={"Hero":"Chakri","Heroin":{"Mylove":"Ekta","MyKeep":"Shivani"}}
print(dictinsidedict.get("Heroin").get("Mylove"))
print(dictinsidedict["Heroin"]["MyKeep"])
dictinsidedict["MyJan"]="Bhoomi"
print(dictinsidedict)
dictinsidedict.pop("MyJan")
print(dictinsidedict)
dictinsidedict["MyJan"]="Bhoomi"
print(dictinsidedict)
dictinsidedict.popitem()
print(dictinsidedict)
print(len(dictinsidedict))
print(dictinsidedict.keys())
print(dictinsidedict.values())
print(dictinsidedict.items())
dictnew.__delitem__()
print(dictnew)
