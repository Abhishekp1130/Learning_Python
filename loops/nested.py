# Nested Loops
for i in range(1, 4):
    for j in range(1, 11):
        print(j)
    print()

for i in range(1, 4):
    for j in range(1, 11):
        print(j, end="")
    print()

# pattern
for i in range(1,6):
    for j in  range (1, i+1):
        print(j, end = "")
    print()