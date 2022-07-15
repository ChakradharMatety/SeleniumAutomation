class A:
    def feature1(self):
        print("Feature is working")

    def faeture2(self):
        print("feature2 is working")

class B:
    def feature3(self):
        print("In Feature3")

class C(A,B):
    def feature4(self):
        print("Feature 4")

    def __int__(self):
        print("Constructor")


obj2=C()
obj2.faeture2()
obj2.feature1()
obj2.feature3()
obj2.feature4()