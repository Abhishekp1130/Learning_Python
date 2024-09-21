A = ["Ross", "Rachel", "Monica", "Joe"]

# program to swap first and fourth element
A[0], A[3] = A[3], A[0]
print(A)

# program to add a value at 2nd position
A.insert(1, "Phoebe")
print(A)

# program to delete a value from 3rd position
A.pop(2)
print(A)

B = [13, 7, 12, 10]
# program to multiply all the numbers in the list
mul = 1
for i in (B):
    mul *= i
print(mul)

# program to get the largest number from the list
B.sort()
print(B)
print()
C = B[-1]
print(f"The largest of the list is {C}")