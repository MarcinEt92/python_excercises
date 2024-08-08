"""
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number. The numbers obtained should be printed
in a comma-separated sequence on a single line.
"""


def are_all_digits_even(number: int):
    number_str = str(number)
    for digit in number_str:
        if int(digit) % 2 != 0:
            return False
    return True


def answer():
    result = []
    min_int = 1000
    max_int = 3000
    for i in range(min_int, max_int + 1):
        if are_all_digits_even(i):
            result.append(str(i))
    print(", ".join(result))


if __name__ == "__main__":
    answer()
