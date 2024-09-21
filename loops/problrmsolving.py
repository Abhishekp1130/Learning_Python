#program to find a sum of all the even numbers upto 50
sum  = 0
for i in range (1, 51):
    if i % 2  == 0:
        sum += i

print(f"the sum of all even numbers is {sum}")

# program to write first 20 numbers and their squared numbers
for i in range(1, 21):
    print(f"the number is {i} and the squared number is {i**2}")

# program to find sum of first 10 odd numbers using while loop
sum = 0
n = 0
while n <= 20:
    if n % 2 != 0:
        sum += n
    n += 1
print(f"the sum of first 10 odd numbers is {sum}")

# program to check if a number is divisble by 8 and 12, upto 100 numbers
for i in range(1, 101):
    if i % 8 == 0 and i % 12 ==0:
        print(i)