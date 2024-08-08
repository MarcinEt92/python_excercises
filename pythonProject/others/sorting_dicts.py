people = [
    {
        "Name": "Gregory",
        "Surname": "Brown",
        "Age": 49,
        "Height": 176
    },
    {
        "Name": "Mark",
        "Surname": "Brown",
        "Age": 45,
        "Height": 191
    },
    {
        "Name": "James",
        "Surname": "Green",
        "Age": 32,
        "Height": 175
    },
    {
        "Name": "John",
        "Surname": "Smith",
        "Age": 26,
        "Height": 168
    },
    {
        "Name": "Andrew",
        "Surname": "Jameson",
        "Age": 26,
        "Height": 184
    },
    {
        "Name": "Martin",
        "Surname": "Jonas",
        "Age": 28,
        "Height": 177
    },
    {
        "Name": "Steven",
        "Surname": "Lake",
        "Age": 62,
        "Height": 198
    },
]


def return_crit(person):
    return person["Age"], person["Name"], person["Surname"]


def temp():
    s = sorted(people, key=lambda p: return_crit(p))
    print(s)


def get_age_and_name(person):
    return person["Age"], person["Name"]


def get_less_than_30(person):
    if person["Age"] < 30 or person["Name"].startswith("S"):
        return True
    else:
        return False


def answer():
    sorted_by_age_and_name = sorted(people, key=get_age_and_name)
    print("\nPeople Sorted By Age And Then Name:")
    print(sorted_by_age_and_name)

    print("\nFilter People Younger than 30:")
    less_than_30 = filter(get_less_than_30, people)
    print(list(less_than_30))


if __name__ == "__main__":
    # answer()
    temp()

    filtered = sorted(people, key=lambda p: (p["Age"], p["Height"]), reverse=True)
    print(list(filtered))
