"""
Level 2

Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
"""


def answer():
    number = input("Provide a number: ")
    how_many = 4
    value = 0
    for i in range(1, how_many + 1):
        value += int(i * number)
    print(f"Value: {value}")


if __name__ == "__main__":
    answer()
