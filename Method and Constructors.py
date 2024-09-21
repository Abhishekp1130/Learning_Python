class DemoClass:
    a = 10

    def shovalue(self):
        self.c = self.a * self.a
        print(self.c)
        # print(self.a)

    def showvalue(self):
        print("Hello World")

    def showvalue1(self, a, b):
        print(a + b)


obj = DemoClass()
obj.shovalue()
obj.showvalue()
obj.showvalue1(20, 30)


class DemoClass1:
    def __init__(self):
        print("Hello World")


obj = DemoClass1()
