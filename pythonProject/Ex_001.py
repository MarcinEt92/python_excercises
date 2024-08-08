"""
Level 1

Question: Write a program which will find all such numbers which are divisible by 7 but are not
a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in
a comma-separated sequence on a single line.
"""


def answer():
    min_val = 2000
    max_value = 3200
    numbers = []
    for number in range(min_val, max_value + 1):
        if number % 7 == 0 and number % 5 != 0:
            numbers.append(str(number))
    print(f"Ex_001 answer:\n")
    print(",".join(numbers))


if __name__ == "__main__":
    answer()
