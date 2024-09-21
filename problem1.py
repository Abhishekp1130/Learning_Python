#  to check number is postive or not
num = int(input("enter the number"))
if num > 0:
    print("positive")
else:
    print("negative")

# odd or even
num1 = int(input("enter the number"))
if num1 % 2 == 0:
    print("even")
else:
    print("odd")


# area calculator
print("Area Calcualtor")
print("""Press 1 to calculate the area of square
Press 2 to calculate the area of rectangle
Press 3 to calculate area of circle
Press 4 to calculate area of triangle""")
choice = int(input("enter the number bw 1 to 4"))
if choice ==1:
    side = float(input("Enter the lenght of the sides:"))
    area = side ** 2
    print("the area of square =", area)
elif choice == 2:
     lenght = float(input("enter the length"))
     width = float(input("enter the width"))
     area = length*width
     print(f"the area is {area}")
elif choice == 3:
    radius = float(input("enter the radius"))
    area = ((22/7)*(radius**2))
    print(f"the area is {area}")
elif choice == 4:
    base = float(input("enter the base of the triangle"))
    height  = float(input("enter the height of the trianglr"))
    area = 0.5*base*height
    print(f"the area of the triangle is{area}")
else:
    print("enter the correct number")

# vowel or not
letter = input("enter a letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print("it is not a vowel")

# check if a number is a single digit number, 2 digit number and so on.... upto 5 digits

num = int(input("enter a number here upto 5 digits: "))
if num >=0 and num<=9:
    print("single digit number")
elif num >=10 and num<=99:
    print("double digit number")
elif num >= 100 and num<=999:
    print("triple digit number")
elif num >= 1000 and num<=9999:
    print("four digit number")
else:
    print("5 digit number")
    















