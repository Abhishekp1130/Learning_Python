import json
d = '{"cname":"Python", "fees":12000, "duration":"2 months"}'

x = json.loads(d)
print(x)

for a in x:
    print(a, x[a])


