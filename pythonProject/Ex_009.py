"""
Level 2

Question Write a program that accepts sequence of lines as input and prints the lines after making
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world Practice makes perfect
Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
"""


class Capitalize:
    @classmethod
    def read_lines_from_user(cls):
        lines = []
        while True:
            line = input("type: ")
            if line == "":
                return lines
            else:
                lines.append(line)

    @classmethod
    def answer(cls):
        lines = cls.read_lines_from_user()
        print("\nAnswer:")
        for line in lines:
            print(line.upper())


if __name__ == "__main__":
    Capitalize.answer()
