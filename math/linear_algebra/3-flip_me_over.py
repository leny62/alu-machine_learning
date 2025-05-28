#!/usr/bin/env python3

"""
Function to matrix transpose.
"""


import numpy as np

"""
Function to return the transpose of a 2D matrix.
"""

def matrix_transpose(matrix):
    """ Returns the transpose of a 2D matrix. """
    return [list(row) for row in zip(*matrix)]  # Unpacks rows as columns

    # Example Usage:
if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]

    print(matrix_transpose(mat1))  # Expected Output: [[1, 3], [2, 4]]
    print(matrix_transpose(mat2))  # Expected Output: [[1, 6, 11, 16, 21, 26], [2, 7, 12, 17, 22, 27], ...]

if __name__ == "__main__":
    matrix_transpose()
