for i in range(15,20):
    print(i)
# for i in range(20):
#     print(i,end=" ")
# for i in range(20):
#     print(20-i,end=' ')
# total=0
# for i in range(101):
#     total=total+i
# print("Total Sum",str(total))
# table=2
# for i in range(11):
#     print(table,"*",i,"=",table*i)
#
# alphabets=['A','B','C','D','E']
# for i in alphabets:
#     print(str(i),end=" ")
#
# for i in range(100):
#     if i%2==0:
#         print(i,end=" ")
# for i in range(100):
#     if i%2!=0:
#         print(i, end=" ")

x=int(input("Enter any number:"))
k=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()
print()

