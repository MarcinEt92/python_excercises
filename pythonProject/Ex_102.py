"""
Cash Machine
"""


def cash_machine():
    values = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0}

    while True:
        amount = input("Enter amount of money to withdraw: ")
        try:
            amount = int(amount)
        except ValueError:
            print("You did not enter a number")
            continue
        if amount % 10 == 0:
            break
        else:
            print("Enter value divisible by 10")
            continue

    for nominal in values.keys():
        values[nominal] = amount // nominal
        amount = amount % nominal

    return values


def answer():
    print("Cash Machine:")
    print(cash_machine())


if __name__ == "__main__":
    answer()
