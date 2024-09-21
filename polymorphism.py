# l = [10, 20, 30, 40, 50]
# print(len(l))
# s = "hello"
# print(len(s))

# Function Overloading
class Ws:
    def displayinfo(self, name=''):
        print("Hello" + name)


obj = Ws()
obj.displayinfo()
obj.displayinfo("Abhi")


# Overriding
class Ws:
    def displayinfo(self):
        print("Hello")


class IIp(Ws):
    def displayinfo(self):
        print("World")


obj = IIp()
obj.displayinfo()


# super keyword

class Ws:
    def displayinfo(self):
        print("Hello")


class IIp(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("World")


obj = IIp()
obj.displayinfo()


