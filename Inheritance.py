# single level inheritance
class A:
    def displayA(self):
        print("Hello  World")


class B(A):
    def displayB(self):
        print("Hello World")


obj=B()
obj.displayA()
obj.displayB()


print("""Multi Level""")

# Multilevel

class A:
    def displayA(self):
        print("Hello  World")


class B(A):
    def displayB(self):
        print("Hello World")

class C(B):
    def displayC(self):
        print("Hello-World")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

# multiple

print("Multiple Inheriatnce")




class A:
    def displayA(self):
        print("Hello  World")


class B():
    def displayB(self):
        print("Hello World")

class C(A,B):
    def displayC(self):
        print("Hello-World")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
