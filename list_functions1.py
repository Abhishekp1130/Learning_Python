a = ["Ironman", "Captian America", "Hulk", "Thor"]

print(len(a))

print(a.count("Hulk"))

a.append("SpiderMan")
print(a)

a.insert(1, "Vision")
print(a)

a.remove("Vision")
print(a)

print(a.pop(4))
print(a)


b=[]
print(b)
b = a.copy()
print(b)

print(a.index("Hulk"))

c = ["vision", "spiderman"]
a.extend(c)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

a.clear()
print(a)