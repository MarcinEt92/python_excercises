"""
Please write a program which accepts a string from console and print it in reverse order.
Ex: rise to vote sir, output: ris etov ot esir
"""


def print_in_reverse_order():
    sequence = input("Enter a sequence: ")
    print(f"Output: {sequence[::-1]}")


if __name__ == "__main__":
    print_in_reverse_order()
