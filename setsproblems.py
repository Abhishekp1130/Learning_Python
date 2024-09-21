# program to find max and min in a set
a = {12, 56, 34, 8, 90, 1, 57}
maximum = max(a)
minimum = min(a)
print(f"the maximum: {maximum}, Minimum: {minimum}")

# program to find common elements in three lists using sets
a = [1, 5, 6, 8, 2]
b = [4, 5, 6, 7]
c = [1, 9, 6, 2, 5]

# z = 23
# z = float(z)
# print(z)

print(set(a) & set(b) & set(c))

# program to find difference betwwen two sets

a = {1, 5, 6, 8, 2}
b = {1, 9, 6, 2, 5}
print(a.difference(b))

# write a program to remove an item from a set if it is present in the set
a = {1, 5, 6, 8, 2}
a.discard(8)
print(a)

# program to check if a set is a subset of another set
a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 4}
print(b.issubset(a))