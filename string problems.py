#program to seperate the following strings into ckoma seperated values
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

b = a.split(".")
print(b)

# program to sort thing alphabetically in python
a = input("enter anything here: ")
b = sorted(a)
print(b)

# program to remove a character from the string
a = "hello"
b = a.replace("l", "b")
print(b)

# program to check the number of occurence of a substring in a stirng
a = "she sells seashells on the sea shore"
g = input("enter the char to search in the string")
b =a.count(g)
print(f"the number of times {g} occurs is {b}")

# take an input from a user as a string then, reverse it.
a = input("enter anything: ")
print(a[::-1])

# to check if a string contains only digit
a = input("enter anything: ")
print(a.isdigit())
if b == True:
    print("it contains only digits")
else:
    print("it contains only digits")

# to check a string is palindrome or not
a = input("enter a string")
rev = a[::-1]

if a ==rev:
    print("the given string is a palindrome")
else:
    print("not a pallindrome")

# program to find number of vowels in a string
a = input("enter anything")
vowels = 0
for i in a:
    if i == "a" or i == "A" or i == "E" or i == "e" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":
        vowels += 1
    print(f"the numbers of vowels ={vowels}")

# program to check if every word in a string begins with a capital letter

a =input("enter")
print(a.istitle())