#!/usr/bin/env python3
"""
Function to compute the shape of a matrix.
"""

def matrix_shape(matrix):
    """ Returns the shape of a matrix as a list of integers. """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]  # Drill down to the next dimension
    return shape

# Example Usage:
if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
            [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]

    print(matrix_shape(mat1))  # Output: [2, 2]
    print(matrix_shape(mat2))  # Output: [2, 3, 5]
