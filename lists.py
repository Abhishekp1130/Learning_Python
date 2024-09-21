fruits = ["apple", "mango", 12, 14.54]
print(type(fruits))

# slicing
a = ["Ironman", "Captian America", "Hulk"]
print(a[2])#indexing starts with 0(zero)

print(a[1:3])
print(a[:2])
print(a[1:])
print(a[::2])
print(a[-3:-1])
print(a[::-1])
print(a[-1:-3:-1])


# Iteration
# Iteration using for loop

a = ["Ironman", "Captian America", "Hulk", "Thor"]
for i in a:
    print(i)

# Iteration using for loop with range and length function
for i in range (len(a)):
    print(a[i])

# iteration using while loop
i = 0
while i < (len(a)):
    print(a[i])
    i += 1


# using Short-Hand For Loop
[print(i) for i in a]



