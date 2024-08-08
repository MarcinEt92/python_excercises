"""
Level 2

Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1..., X-1; j=0,1,¡­Y-1.
Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def generate_2d_array(x, y):
    """
    Generates 2d array where i-th row and j-th column of the array should be i*j
    :param x: 1st dimension
    :param y: 2nd dimension
    :return: 2d array, list of lists
    """
    array_2d = []
    for i in range(0, x):
        array_2d.append([])
        for j in range(0, y):
            array_2d[i].append(i * j)
    return array_2d


def test_generate_2d_array():
    x = 3
    y = 5
    array_2d = generate_2d_array(x, y)
    print(array_2d)


if __name__ == "__main__":
    test_generate_2d_array()
