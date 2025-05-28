#!/usr/bin/env python3

"""
Function to np transpose.
"""


"""
Function to return the transpose of a NumPy array.
"""

import numpy as np

def np_transpose(matrix):
    """ Returns the transpose of a numpy.ndarray. """
    return matrix.T  # Uses NumPy's built-in transpose method

    # Example Usage:
if __name__ == '__main__':
    mat1 = np.array([1, 2, 3, 4, 5, 6])
    mat2 = np.array([])
    mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
    [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

    print(np_transpose(mat1))  # Expected Output: [1 2 3 4 5 6]
    print(np_transpose(mat2))  # Expected Output: []
    print(np_transpose(mat3))  # Expected Output: Transposed multi-dimensional matrix

if __name__ == "__main__":
    np_transpose()
