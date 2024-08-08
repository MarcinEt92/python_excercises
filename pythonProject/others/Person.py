"""
https://www.studocu.com/pl/document/politechnika-czestochowska/podstawy-programowania/pp-lista-12-2023-2024/95773697
"""
from datetime import datetime


class Person:
    static_id = 0

    def __init__(self, name: str, surname: str, birth_year: int, email: str):
        assert 1900 < birth_year <= datetime.now().year
        assert "@" in email

        self.id = Person.static_id
        Person.static_id += 1

        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.email = email

    def __repr__(self):
        return f"Person({self.name}, {self.surname}, born in: {self.birth_year})"

    @classmethod
    def instantiate_from_csv(cls, path):
        contacts = []
        with open(path, "r") as f:
            people = f.readlines()
            print("")
            for person in people[1:]:
                person = person.strip().split(",")
                contacts.append(
                    Person(
                        name=person[0],
                        surname=person[1],
                        birth_year=int(person[2]),
                        email=person[3]
                    )
                )

        return contacts


class Program:
    @classmethod
    def _get_id(cls, person, identifier):
        if person.id == identifier:
            return True
        else:
            return False

    @classmethod
    def run(cls):
        # Print sample contact list
        contacts = Person.instantiate_from_csv("person.csv")
        print(contacts)

        # Search By ID:
        person_id = 2
        filtered = filter(lambda person: cls._get_id(person, person_id), contacts)
        # filtered = filter(lambda person: person.id == 1, contacts)
        print('-----------------------------------')
        print(*filtered)


if __name__ == "__main__":
    Program.run()
