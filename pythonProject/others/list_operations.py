"""
Write a Python program to sum all the items in a list.
"""


def sum_all_items():
    s = 0
    numbers_list = [1, 2, 3, 4, 5]
    for number in numbers_list:
        s += number
    print(f"1.a. Sum of numbers in list: {s}")
    print(f"1.b. Sum of numbers in list: {sum(numbers_list)}")


def multiply_nums_in_list():
    s = 1
    numbers_list = [1, 2, 3, 4, 5, 4, 3, 2]
    for number in numbers_list:
        s *= number
    print(f"2. Numbers multiplied: {s}")


def get_max_from_list():
    numbers_list = [1, 2, 3, 4, 5]
    maximum = max(numbers_list)
    print(f"Max: {maximum}")


def get_min_from_list():
    numbers = [1, 2, 3, 4, 5, 4, 3, 2]
    min_value = min(numbers)
    print(f"Min Value: {min_value}")


def calculate_custom_1():
    sample_list = ['abc', 'xyz', 'aba', '1221']
    res = 0
    for word in sample_list:
        if len(word) > 2 and word[0] == word[-1]:
            res += 1
    print(f"Number of words that meet criteria is: {res}")


def _sort_helper(x):
    return x[1], x[0]


def sort_list_01():
    sample = [(3, 5), (2, 5), (3, 2), (2, 2), (1, 2), (4, 4), (2, 3), (2, 1)]
    sample_sorted = sorted(sample, key=lambda x: (x[1], x[0]))
    print(f"Sorted list: {sample_sorted}")


def remove_duplicates():
    list_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
    no_duplicates_list = list(set(list_duplicates))
    print(f"No duplicates: {no_duplicates_list}")


def _sort_helper2(x):
    return len(x), x


def sort_list_02():
    my_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    ms = sorted(my_list, key=_sort_helper2)
    print(f"Sorted list: {ms}")


def copy_list():
    list1 = [1, 2, 3, [4, 5]]
    list2 = list(list1)
    print(list1)
    print(list2)

    list1[0] = 9
    list1[3].append(6)
    print(list1)
    print(list2)


def answer():
    sort_list_02()


if __name__ == "__main__":
    answer()
