#!/usr/bin/env python3
"""
Function to perform matrix multiplication.
"""

def mat_mul(mat1, mat2):
    """ Returns the matrix multiplication of mat1 and mat2, or None if they cannot be multiplied. """
    if len(mat1[0]) != len(mat2):
        return None
    
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]

if __name__ == '__main__':
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]

    print(mat_mul(mat1, mat2))
