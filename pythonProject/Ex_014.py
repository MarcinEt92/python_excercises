"""
Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case
letters. Suppose the following input is supplied to the program:
Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
"""


def calculate_upper_and_lower(sequence: str):
    upper_lower_dict = {
        "upper": 0,
        "lower": 0
    }
    for sign in sequence:
        if sign.isalpha():
            if sign.isupper():
                upper_lower_dict["upper"] += 1
            if sign.islower():
                upper_lower_dict["lower"] += 1
    return upper_lower_dict


def answer():
    sequence = "Hello world 123!"
    lower_upper = calculate_upper_and_lower(sequence)
    print(f"UPPER CASE {lower_upper['upper']} LOWER CASE {lower_upper['lower']}")


if __name__ == "__main__":
    answer()
