"""
Level 2

Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
printed in a comma separated sequence.
Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
"""


def get_binaries_divisible_by_5(sequence: str):
    results = []
    binaries = sequence.split(",")
    for element in binaries:
        element = element.strip()
        try:
            num = int(element, 2)
        except ValueError:
            print(f"Value {element} cannot be converted to a number")
            continue
        if num % 5 == 0:
            results.append(bin(num)[2:])
    return results


def answer():
    sequence = input("Enter a sequence of binary numbers: ")
    results = get_binaries_divisible_by_5(sequence)
    print("Bin numbers divisible by 5:")
    print(','.join(results))


if __name__ == "__main__":
    answer()
