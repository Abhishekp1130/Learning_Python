
a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor"}
# union
print(a.union(c))

# Difference
print(a.difference(c))

# difference update
a.difference_update(c)
print(a)

# intersection
x = (a.intersection(c))
print(x)

a.intersection_update(c)
print(a)

