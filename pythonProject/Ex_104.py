"""
Palindrome
"""


def check_is_palindrome(user_in: str):
    user_in = user_in.strip().lower()
    return user_in == user_in[::-1]


def answer():
    sample_ins = ("Ala", "KamilSlimak ", "Ale")
    sample_ins_reversed = reversed(sample_ins)
    for sample in sample_ins_reversed:
        print(f"Is {sample} a palindrome: {check_is_palindrome(sample)}")



if __name__ == "__main__":
    answer()
