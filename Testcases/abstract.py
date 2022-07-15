# Abstract Class cant create object
# Can't instantiate abstract class
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def hello(self):
        print("Hello World")

class Keyboard(Computer):
    def process(self):
        print("Running++")

c=Keyboard()
c.process()
c.hello()

list=[2,3,4,5]
it=iter(list)
print(it.__next__())
print(next(it))



