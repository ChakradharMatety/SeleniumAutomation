mylist1 = [11, 11, 20, 30, 40]
mylist2 = [22, 11, 20, 22, 40]


def remove_list_val(val, lists):
    lists.remove(val)
    print("Val " + str(val) + "  removed from the list  " + str(lists))


remove_list_val(20, mylist1)
remove_list_val(40,mylist2)
