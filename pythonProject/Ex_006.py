"""
Level 2

Question: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example Let us assume the following comma separated input sequence is given to the program:
100,150,180 The output of the program should be: 18,22,24
"""
import math


class Calculations:
    C = 50
    H = 30

    @classmethod
    def _calculate_rounded_q(cls, d):
        return round(math.sqrt((2 * cls.C * d) / cls.H))

    @classmethod
    def test_calculate_q(cls):
        results = []
        input_values = input("Provide Values To Calculate: ")
        values_list = input_values.split(",")
        for value in values_list:
            try:
                d = float(value)
            except ValueError:
                print(f"Value {value} provided is not a number")
                continue
            q = cls._calculate_rounded_q(d)
            results.append(q)
        print(*results)


if __name__ == "__main__":
    Calculations.test_calculate_q()
