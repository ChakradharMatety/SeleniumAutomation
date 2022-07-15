Fruits={"Mango","Apple","Grapes","Orange","Banana"}
# for i in Fruits:
#     print(i)

# eatables=Fruits.__iter__()
# print(eatables.__next__())
# print(eatables.__next__())
# print(eatables.__next__())
# print(eatables.__next__())
# print(eatables.__next__())
looper=iter(Fruits)
while True:
    try:
        print(looper.__next__())
    except Exception as e:
        break







