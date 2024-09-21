# while true.
n = int(input("number"))
while True:
    print(n)
    n += 1
    if n >= 2:
        break

while True:
    num1 = int(input("enter a number"))
    num2 = int(input("enter another number"))

    print(num1 + num2)
    repeat = input("do you want to stop the program(Y)")
    if repeat == "Y":
        break
