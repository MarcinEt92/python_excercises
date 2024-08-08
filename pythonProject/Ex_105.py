"""
extract 2 dmin list into 1d list
"""


def extract_to_1d_list(two_dim_list: list):
    result = []
    for element in two_dim_list:
        result.extend(element)
    return result


def extract_to_1d_list_second_ways(two_dim_list: list):
    result = []
    for element in two_dim_list:
        for i in range(0, len(element)):
            result.append(element[i])
    return result



def answer():
    sample_list = [[1, 2], [3, 4], [8, 9, 10]]
    list_extracted = extract_to_1d_list(sample_list)
    list_extracted_second_way = extract_to_1d_list_second_ways(sample_list)
    print(f"List converted to one dimension list: {list_extracted}")
    print(f"List converted to one dimension list: {list_extracted_second_way}")


if __name__ == "__main__":
    answer()
