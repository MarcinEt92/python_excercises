"""
Input from user and get reversed string and its length
"""


def get_reversed_and_len():
    while True:
        user_in = input("Enter phrase: ")
        user_in = user_in.strip()
        if user_in == "":
            print("Provide non ampty phrase")
            continue
        return user_in[::-1], len(user_in)
    


def answer():
    print("Get Str Reverse and len")
    result = get_reversed_and_len()
    print(f"Str reversed: {result[0]}, length: {result[1]}")


if __name__ == "__main__":
    answer()

