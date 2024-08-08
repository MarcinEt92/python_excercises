"""
Cesar cipher
"""
import string


def transform_to_cesar(sentence: str, shift_num: int):
    result = ""
    alphabet = string.ascii_lowercase
    for letter in sentence:
        is_lower = letter.islower()
        letter = letter.lower()
        if letter.isalpha():
            index = alphabet.index(letter)
            if index + shift_num >= len(alphabet):
                pos = index + shift_num - len(alphabet)
            else:
                pos = index + shift_num
            if is_lower:
                result += alphabet[pos]
            else:
                result += alphabet[pos].upper()
        else:
            result += letter
    return result


def transform_to_cesar_translate(sentence: str, shift_num: int):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift_num:] + alphabet[0:shift_num]
    translation = str.maketrans(alphabet, shifted_alphabet)
    return sentence.translate(translation)


def answer():
    sentence = "ala ma kota, a kot ma ale"
    shift_num = -21
    print(f"{sentence} ciphered: {transform_to_cesar(sentence, shift_num)}")
    print(f"{sentence} ciphered: {transform_to_cesar_translate(sentence, shift_num)}")


if __name__ == "__main__":
    answer()
