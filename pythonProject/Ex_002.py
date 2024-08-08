"""
Level 1

Question: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
"""


class Factorial:
    @classmethod
    def _factorial(cls, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @classmethod
    def test_factorial(cls):
        number = 8
        print(f"Factorial of {number} is {cls._factorial(number)}")


if __name__ == "__main__":
    Factorial.test_factorial()
