Employee_Data = {"name": "John",
                 "age": "24",
                 "gender": "male",
                 "position": "associate"
                 }

print(Employee_Data)
# accessing data
print(Employee_Data["age"])

# iteration
# to print all keys
for x in Employee_Data:
    print(x)

#print all the value names one by one
for x in Employee_Data:
    print(Employee_Data[x])

# using value functions
for x in Employee_Data.values():
    print(x)


# usin items function
for x,y in Employee_Data.items():
    print(x,"->",y)


# Functions

# get
x = Employee_Data.get("name")
print(x)

# item
a = Employee_Data.items()
print(a)

# keys
b =Employee_Data.keys()
print(b)


# values
c = Employee_Data.values()
print(c)

# copy
d = Employee_Data.copy()
print(d)

# setdefault
x = Employee_Data.setdefault("gender","Female")
print(x)

Employee_Data.update({"age": "25"})
print(Employee_Data["age"])
print(Employee_Data)

# pop
Employee_Data.pop("age")

print(Employee_Data)

# pop_item
Employee_Data.popitem()
print(Employee_Data)

# clear
Employee_Data.clear()
print(Employee_Data)


# nested dictonary
Data = {1:{"name": "John",
                 "age": "24",
                 "gender": "male",
                 "position": "associate"},
           2:{"name": "Lisa",
                 "age": "26",
                 "gender": "Female",
                 "position": "Sr.associate"}}
print(Data)
print(Data[1])
print(Data[2]["age"])
