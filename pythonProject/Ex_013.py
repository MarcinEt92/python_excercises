"""
Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be:
LETTERS 10 DIGITS 3
"""


def calculate_nums_and_digits(sequence: str):
    count_dict = {
        "letters": 0,
        "digits": 0
    }
    for sign in sequence:
        if sign.isalpha():
            count_dict["letters"] += 1
        elif sign.isdigit():
            count_dict["digits"] += 1
    return count_dict


def answer():
    sequence = input("Type a sequence: ")
    letters_digits = calculate_nums_and_digits(sequence)
    print(f"LETTERS: {letters_digits['letters']} DIGITS: {letters_digits['digits']}")


if __name__ == "__main__":
    answer()
