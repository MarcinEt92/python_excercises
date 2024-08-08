"""
Level 1

Question: Write a program which accepts a sequence of comma-separated numbers from console and
generate a list and a tuple which contains every number. Suppose the following input is
supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
"""


def are_all_values_numbers(collection):
    for value in collection:
        try:
            float(value)
        except ValueError:
            return False
    return True


def answer():
    input_values = input("enter numbers separated by commas: ")
    split_values = input_values.split(",")
    split_values_tuple = tuple(split_values)
    if are_all_values_numbers(split_values):
        print(f"Output: {split_values} {split_values_tuple}")
    else:
        print("You provided some values that are not numbers")


if __name__ == "__main__":
    answer()
