a = "apple", "mango", "banana", 1, 67, 1.23
print(type(a))

# slicing
a = "Oneplus", "Samsung", "Redmi", "Nokia", "Moto"
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[1::2])
print(a[::-1])
print(a[2::-1])


# iteration
# for loop
for i in a:
    print(i)




# with range and length
for i in range (len(a)):
    print(a[i])




# while loop
i = 0
while i < len(a):
    print(a[i])
    i+=1

a = "Oneplus", "Samsung", "Redmi", "Nokia", "Moto"
print("before conversion", type(a))
a = list(a)
print("after conversion", type(a))
a.append("Apple")
a = tuple(a)
print(a)


# tuple functions
print(a.count("Redmi"))
print(a.index("Nokia"))