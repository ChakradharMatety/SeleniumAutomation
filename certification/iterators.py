mylist = [1, 2, 3, 4, 5]
my_iter = iter(mylist)
while True:
    try:
        print(my_iter.__next__())
    except StopIteration:
        break
#
# for i in mylist:
#     print(i)

# while True:
#     print(my_iter.__next__())
