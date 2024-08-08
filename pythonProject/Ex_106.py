"""
Wypisz obiekty klasy
"""


class Person:
    people = []

    def __init__(self, name: str, surname: str):
        assert len(name) > 0, "Name length should be greater than 0"
        assert len(surname) > 0, "Surname length should be greater than 0"
        
        self.name = name
        self.surname = surname

        Person.people.append(self)


    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"Name: {self.name}, Surname={self.surname}"



def answer():
    p1 = Person("Anna", "Kowalska")
    p2 = Person("Marek", "Malinowski")
    print(Person.people)
    print(p2)


if __name__ == "__main__":
    answer()
