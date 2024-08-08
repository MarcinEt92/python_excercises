"""
Level 1

Question: Define a class which has at least two methods: getString: to get a string from console
input printString: to print the string in upper case.
Please include simple test function to test the class methods.
"""


class StringOperations:
    @classmethod
    def get_string(cls):
        input_value = input("Write a sequence of words: ")
        return input_value

    @classmethod
    def print_string(cls, sequence: str):
        """
        Prints string in upper case
        :param sequence: sequence of chars
        :return: none
        """
        print(sequence.upper())

    @classmethod
    def test_print_string(cls):
        input_value = cls.get_string()
        cls.print_string(input_value)


if __name__ == "__main__":
    StringOperations.test_print_string()
