"""
Level 2

Question: Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
"""


def are_sequence_alphabetical(sequence):
    for element in sequence:
        if not element.isalpha():
            return False
    return True


def test_sort_words():
    sequence = input("Enter a sequence: ")
    sequence_list = sequence.split(",")
    if are_sequence_alphabetical(sequence_list):
        sequence_list.sort()
        print(",".join(sequence_list))
    else:
        print("Provided values are not alphabetical, please provide correct ones")


if __name__ == "__main__":
    test_sort_words()
