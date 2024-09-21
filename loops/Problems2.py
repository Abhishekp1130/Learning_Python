# Fibonacci Series up to 10 numbers
a = 0
b = 1
n = int(input("enter a number here: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

# check if a number is prime or not
num = int(input("enter a number here: "))

if num <= 1:
    print("it is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("number is not a prime number")
            break
    else:
        print("it is a prime number")
# find a palindrome of integers
num = int(input("enter a number here: "))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if rev == temp:
    print("it is palindrome")
else:
    print("it is not a palindrome")

# create an area calculator
print("Area Calcualtor")
while True:
    print("""Press 1 to calculate the area of square
    Press 2 to calculate the area of rectangle
    Press 3 to calculate area of circle
    Press 4 to calculate area of triangle""")
    choice = int(input("enter the number bw 1 to 4"))
    if choice == 1:
        while True:
            side = float(input("Enter the lenght of the sides:"))
            area = side ** 2
            print("the area of square =", area)
            repeat = input("do you want to try again with square?")
            if repeat == "no":
                break
    elif choice == 2:
        while True:
            length = float(input("enter the length"))
            width = float(input("enter the width"))
            area = length * width
            print(f"the area is {area}")
            repeat = input("do you want to try again with rectanle?")
            if repeat == "no":
                break
    elif choice == 3:
        while True:
            radius = float(input("enter the radius"))
            area = ((22 / 7) * (radius ** 2))
            print(f"the area is {area}")
            repeat = input("do you want to try again with circle?")
            if repeat == "no":
                break
    elif choice == 4:
        while True:
            base = float(input("enter the base of the triangle"))
            height = float(input("enter the height of the trianglr"))
            area = 0.5 * base * height
            print(f"the area of the triangle is{area}")
            repeat = input("do you want to try again with circle?")
            if repeat == "no":
                break
    repeat1 = input("do you want to repeat the menu again? ")
    if repeat1 == "no":
        break



