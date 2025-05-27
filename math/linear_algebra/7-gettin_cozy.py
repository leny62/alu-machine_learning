#!/usr/bin/env python3
"""
Function to concatenate two 2D matrices along a specific axis.
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """ Returns a new matrix by concatenating mat1 and mat2 along the given axis. """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]

    return None


if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]

    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)

    print(mat4)
    print(mat5)
