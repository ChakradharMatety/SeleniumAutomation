class my_class:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def get_details(self):
        print(f"Name:{self.name}\n Age:{self.age}\n Dob:{self.dob}")


obj = my_class("Chakradhar", "35", "04-02-1987")
# obj.get_details()
# obj.age=26
# obj.get_details()
# del obj.dob
obj.get_details()

squares=[x**2 for x in range(1,100)]
print(squares)
