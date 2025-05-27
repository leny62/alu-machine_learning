#!/usr/bin/env python3
"""
Function to add two 2D matrices element-wise.
"""

def add_matrices2D(mat1, mat2):
    """ Returns the element-wise sum of two matrices, or None if shapes mismatch. """
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None
    return [[row1[i] + row2[i] for i in range(len(row1))] for row1, row2 in zip(mat1, mat2)]

# Example Usage:
if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]

    print(add_matrices2D(mat1, mat2))  # Expected Output: [[6, 8], [10, 12]]
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))  # Expected Output: None
