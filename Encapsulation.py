# Getter and Setter

class Student:
    def __init__(self):
        self.__name = ""

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name


obj = Student()
obj.setname("Testing")
name = obj.getname()
print(name)


# encapsulation

class Student:
    __name = "Ravi"


obj = Student()
print(obj.__name)


# using constructor
class Student:
    __name = "Ravi"

    def __init__(self):
        print(self.__name)  # Accessing the private attribute within the class
        self.__displayinfo()  # Calling a private method

    def __displayinfo(self):
        print("Welcome to My Coding World")


obj = Student()

