"""
Level 2

Question: Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be: again and hello makes perfect practice world
"""


def answer():
    words = input("Enter words: ")
    words = list(set(words.split(" ")))
    words.sort()
    print(f"Output:\n{words}")


if __name__ == "__main__":
    answer()

