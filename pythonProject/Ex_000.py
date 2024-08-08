"""
Palindrome check
"""


def is_palindrome(word: str):
    """
    Checks if provided word is a palindrome or not
    :param word: sequence of characters to check
    :return: True if word is palindrome, False otherwise
    """
    return word == word[::-1]


def test_is_palindrome():
    palindrome = "abba"
    not_palindrome = "alabama"
    print(f"{palindrome} is palindrome: {is_palindrome(palindrome)}")
    print(f"{not_palindrome} is palindrome: {is_palindrome(not_palindrome)}")


if __name__ == "__main__":
    test_is_palindrome()
