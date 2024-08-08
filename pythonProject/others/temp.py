"""
sorting dict by value
"""
import operator


a = {
    "Surname": "Novak",
    "Name": "Mark",
    "Country": "Turkey",
    "City": "Ankara"
}

a.update({"Job": "Accountant"})

b = sorted(a.items(), key=lambda item: item[1])

for k, v in a.items():
    print(f"{k} -> {v}")

num_d = {}

for i in range(1, 6):
    num_d.update({i: i*i})

print(num_d)

print(sum(num_d.values()))

sd = sorted(a.items(), key=lambda item: item[1])
print(dict(sd))

print(max(num_d.values()))


