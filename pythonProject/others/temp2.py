class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"Guy {self.name} {self.surname}"


p = Person("Mark", "Novak")
p2 = Person("Mark", "Novak")
print(p)

print(p.__dict__)

dupl_d = {"a": 1, "b": 2, "c": 3, "d": 1, "e": 2, "f": 8}
no_d_d = {}
for k, v in dupl_d.items():
    if v not in no_d_d.values():
        no_d_d.update({k: v})

print(no_d_d)
