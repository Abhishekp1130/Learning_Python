a = {"Ironman", "Hulk", "Thor", "Captain America"}
print(a)
for x in a:
    print(x)

# functions
# add
a.add("Spidy")
print(a)

# pop
a.pop()
print(a)

# remove
a.remove("Thor")
print(a)

# discard
a.discard("Hulk")
print(a)

# copy
b = a.copy()
print(b)


a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor"}

# isdisjoint
print(a.isdisjoint(c))


# issubset
print(a.issubset(b))
print(c.issubset(a))

# issuperset
print(b.issuperset(a))

# update
a.update(c)
print(a)

# clear
a.clear()
print(a)
