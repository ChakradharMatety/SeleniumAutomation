# Object is an instance of a class
# Object is anything in this space which has some properties(varibles) and can perform some actions(methods)
# Class is a blueprint of an object
# Class is an entity / a module which can bind data members(class variables and it methods) together.
# self means instance of the current class

class Person:

    def welcome(self):
        print("Hello Python")

    def sum(self,num1,num2):
        print(num1+num2)

def hello_world():
        print("Hello World")



p=Person()
hello_world()
print(p.welcome)
p.sum(num1=10,num2=20)
p.sum(60,30)
p.name="Chakra"
p.color="Brown"
print(p.name)


