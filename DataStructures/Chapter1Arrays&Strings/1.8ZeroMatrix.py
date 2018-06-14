# O(mn) space(1) or space(n)
# Using comments and TODOs to explain the code, focus on the important question

import unittest

def zero_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # temp = []
    #
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j] == 0:
    #             temp.append((i, j))
    #
    # for i, j in temp:
    #     for row in range(m):
    #         matrix[i][row] = 0
    #     for col in range(n):
    #         matrix[col][j] = 0
    #
    # return matrix

# We can use the matrix row and col set the flags so it take O(1) Space
    firstColHasZero, firstRowHasZero = False, False

    for i in range(n):
        if matrix[i][0] == 0:
            firstColHasZero = True
            break

    for j in range(m):
        if matrix[0][j] == 0:
            firstRowHasZero = True
            break

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(1, m):
                matrix[i][j] = 0

    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(1, n):
                matrix[i][j] = 0

    if firstColHasZero:
        for i in range(n):
            matrix[i][0] = 0

    if firstRowHasZero:
        for j in range(m):
            matrix[0][j] = 0

    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()