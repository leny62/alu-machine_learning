#!/usr/bin/env python3
"""
Function to concatenate two 2D matrices along a specific axis.
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """ Returns a new matrix by concatenating mat1 and mat2 along the given axis. """
    if axis == 0:  # Concatenate along rows
        if len(mat1[0]) != len(mat2[0]):  # Ensure column count matches
            return None
        return mat1 + mat2  # Concatenation along rows

    elif axis == 1:  # Concatenate along columns
        if len(mat1) != len(mat2):  # Ensure row count matches
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]  # Element-wise row concatenation

    return None  # Invalid axis

# Example Usage:
if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]

    mat4 = cat_matrices2D(mat1, mat2)  # Expected Output: [[1, 2], [3, 4], [5, 6]]
    mat5 = cat_matrices2D(mat1, mat3, axis=1)  # Expected Output: [[1, 2, 7], [3, 4, 8]]

    print(mat4)
    print(mat5)
