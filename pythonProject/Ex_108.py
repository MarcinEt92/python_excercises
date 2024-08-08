"""
count occurrences of pairs
xxcbaa
xxcdaa
"""


def count_occurrences(word_this: str, word_other: str):
    common_pairs = []
    count = 0
    for i in range(0, len(word_this) - 1):
        if word_this[i:i+2] in word_other:
            common_pairs.append(word_this[i:i+2])
            count += 1
    return common_pairs, count


def answer():
    word_this = "xxcbaa"
    word_other = "xxcdaa"
    results = count_occurrences(word_this, word_other)
    print(f"How many pairs: {results[1]}, and pairs are: {results[0]}")


if __name__ == "__main__":
    answer()
