mylist = [11, 11, 20, 30, 40]


def is_duplicate(val):
    print(mylist.count(val))
    if mylist.count(val) > 1:
        print("Duplicates Found for value: " + str(val))
    else:
        print("No Duplicates Found for value: " + str(val))


is_duplicate(11)
is_duplicate(20)
