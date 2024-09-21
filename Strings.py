a = "Hello World "
print(len(a))  # length
print(a.count("o"))  # count
print(a.upper())
print(a.lower())
print(a.index("o"))

# capitalize
b = "hello world"
print(b.capitalize())
# find
print(b.find("l"))

# isalnum
a = "Hello124"
print(a.isalnum())

# isalpha
a = "LLo"
print(a.isalpha())

c = "1267"
print(c.isdecimal())
print(c.isdigit())
print(c.isnumeric())

d = "Harry Potter"
print(d.istitle())

a = "Hello"
print(a.endswith("o"))
print(a.startswith("H"))

b = "HellO"
print(b.swapcase())

b = "      HellO    "
print(b.strip())

c = "#hello#world#Thanks#Hpy"
print(c.split("#"))

d = "HEllo"
x = d.ljust(20, "#")
print(x, "is a happpy day")
h = d.rjust(20, "#")
print(h, "is a happpy day")

f = "Fuck you John"
print(f.replace("John", "sunil"))

# rindex
a = "Hello World Thank You For Taking Up My Course"
print(a.rindex("You"))
print(a.rfind("You"))

# slicing
a = "Hello World Thank You For Taking Up My Course"
print(a[0:5])
print(a[0:5:2])#step
b = "0123456789"
print(b[::-1])#reverse
print(b[6::-1])#upto 6