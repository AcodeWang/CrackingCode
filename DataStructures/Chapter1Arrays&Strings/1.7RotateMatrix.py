
# O(n^2), Space(1) in place

# Python list reverse :
# 1. reversed(list)
# 2. range(len(list)-1, -1, -1) (-1, len(list-1)],  range(1,5,2) [1,3,5]
# Slice : operation array(0:) a[0] included. array(:6) a[6] not included
# 3. x in array(::-1)

import unittest


# Space(n^2)
def rotate_matrix_space_n2(test_matrix):

    n = len(test_matrix)

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = test_matrix[n-1-j][i]

    return matrix


# Space(1)
def rotate_matrix(matrix):
    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            matrix[i][-layer-1] = temp

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()