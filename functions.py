def hell():
    print("hello")


hell()


# parameter and arguments
def add(x, y):  # x and y are the parameters
    print(x + y)


add(3, 6)  # values are the arguments


# area of a rectangle
def rect(length, width):
    a = length * width
    print(f"the area of the rectangle is: {a}")


rect(4, 8)


# arbitary arguments
def hello(*name):
    print("hello my name is ", name[0])


hello("john", "lisa", "peter")


# return statement


def hello():
    return ("Hello World")


print(hello())


# recursion
# def hello():
#     print("HEllo")
#     return hello()
#
#
# print(hello())


# factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))

# lambda function
a = lambda b: b * 5
print(a(4))

x = lambda a, b, c: (a + b) * c
print(x(3, 7, 3))

# local variables
x = 24

print(f"the first variable x: {x}")


def hello():
    x = 25
    return x


print(hello())

print(x)

# global

x = 24
print(f"first variable x: {x}")


def hello():
    global x
    x = 25
    return x


print(hello())

print(x)




