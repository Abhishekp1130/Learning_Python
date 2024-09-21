import json
file = open("1.json", "r")
final = file.read()
finaldata = json.loads(final)
print(finaldata)

for a in finaldata:
    print(a)
    print(a[0])
finaldata['new_key'] = "new_value"


with open("1.json", "w") as file:
    json.dump(finaldata, file, indent=4)  

print("New data added and file written successfully!")