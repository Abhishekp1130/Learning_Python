# Arithmetic operator
print(8%3)
print (float(8//3))
print(2**2)

#comparison operators
print(3<6)
print(3>6)
print(3==3)
print(3!=3)
print(10>=3)

#logical operators
a = 3>2 and 8<7
# and
print(a)
b = 3>2 or 8<7
# or
print(b)
c = 3>2 or 8<7
# not
print(not(c))

# assignment operator
x = 6
print(x)
y = 0
y += 1
print(y)

z = 6
z -= 1
print(z)

# identity operator
a = 123
b = 123
print(a is b)
print(a is not b)

# bitwise operator
print(bin(1))
a =10
b =8
print(a & b)

x = 10
y = 8
print (x | y)

print(x ^ y)

g =10
# left shift
print(g >> 1)
#right shift
print(g << 1)


# membership operator
a = "hello"

print("e" in a)
print("e" not in a)