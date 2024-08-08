"""
Find the longest common subsequence of 2 lists, e.g.
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [6, 7, 5, 6, 7, 8]

result should be [5, 6, 7, 8]
"""

"""
longest common subsequence

"""


def find_min_subseq(nums1, nums2):
    nums_min = min(nums1, nums2, key=lambda x: len(x))
    nums_max = max(nums1, nums2, key=lambda x: len(x))
    for i in range(0, len(nums_min)):
        for j in range(0, len(nums_min) - i):
            sublist = nums_min[j:j+i+1]
            sublist_str = str(sublist).strip("[]")
            if sublist_str in str(nums_max):
                return sublist
    return []


def find_longest_subseq_better(nums1, nums2):
    nums_min = min(nums1, nums2, key=lambda x: len(x))
    nums_max = max(nums1, nums2, key=lambda x: len(x))
    for i in range(0, len(nums_min)):
        for j in range(0, i+1):
            sublist = nums_min[j:len(nums_min)-i+j]
            sublist_str = str(sublist).strip("[]")
            if sublist_str in str(nums_max):
                return sublist
    return []


def temp():
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [6, 7, 5, 6, 7, 8]
    # nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # nums2 = [9, 10, 11]
    longest_subseq = find_longest_subseq_better(nums1, nums2)
    shortest_subseq = find_min_subseq(nums1, nums2)
    print(f"Longest subsequence: {longest_subseq} with length of {len(longest_subseq)}")
    print(f"Shortest subsequence: {shortest_subseq} with length of {len(shortest_subseq)}")


def answer():
    temp()


if __name__ == "__main__":
    answer()
