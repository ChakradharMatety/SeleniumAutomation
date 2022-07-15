# Function is a piece of program(set of instructions) to perform some task
def helloworld():
    print("hello python")


def sum(num1,num2):
    result= num1+num2
    print("result is",result)


def mul(num1,num2,num3):
    result=num1*num2*num3
    return result

helloworld()
sum(1,5)
print(mul(2,3,4))