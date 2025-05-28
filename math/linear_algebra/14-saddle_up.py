#!/usr/bin/env python3

"""
Function to np matmul.
"""


"""
Function to perform matrix multiplication using NumPy.
"""

import numpy as np

def np_matmul(mat1, mat2):
    """ Returns the matrix multiplication of mat1 and mat2. """
    return np.matmul(mat1, mat2)  # Uses NumPy's built-in matrix multiplication function

    # Example Usage:
if __name__ == '__main__':
    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat3 = np.array([[7], [8], [9]])

    print(np_matmul(mat1, mat2))  # Expected Output: [[330, 396, 462], [726, 891, 1056]]
    print(np_matmul(mat1, mat3))  # Expected Output: [[550], [1342]]

if __name__ == "__main__":
    np_matmul()
