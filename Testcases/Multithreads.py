from threading import *
from time import sleep

import self as self


class Person(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Thread1 ",end="")


class Humans(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Thread2 ",end="")


t1 = Person()
t2 = Humans()
t1.start()
t2.start()


