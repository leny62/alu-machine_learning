#!/usr/bin/env python3
"""
Function to recursively add two matrices element-wise.
"""

def add_matrices(mat1, mat2):
    """ Returns the element-wise sum of two matrices, or None if shapes mismatch. """
    if type(mat1) != type(mat2) or len(mat1) != len(mat2):
        return None
    if isinstance(mat1, list):
        return [add_matrices(m1, m2) for m1, m2 in zip(mat1, mat2)]
    return mat1 + mat2

# Example Usage:
if __name__ == '__main__':
    mat1 = [1, 2, 3]
    mat2 = [4, 5, 6]
    mat3 = [[1, 2], [3, 4]]
    mat4 = [[5, 6], [7, 8]]

    mat5 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
             [[9, 10, 11, 12], [13, 14, 15, 16]],
             [[17, 18, 19, 20], [21, 22, 23, 24]]],
            [[[25, 26, 27, 28], [29, 30, 31, 32]],
             [[33, 34, 35, 36], [37, 38, 39, 40]],
             [[41, 42, 43, 44], [45, 46, 47, 48]]]]

    mat6 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
             [[19, 110, 111, 112], [113, 114, 115, 116]],
             [[117, 118, 119, 120], [121, 122, 123, 124]]],
            [[[125, 126, 127, 128], [129, 130, 131, 132]],
             [[133, 134, 135, 136], [137, 138, 139, 140]],
             [[141, 142, 143, 144], [145, 146, 147, 148]]]]

    mat7 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
             [[117, 118, 119, 120], [121, 122, 123, 124]]],
            [[[125, 126, 127, 128], [129, 130, 131, 132]],
             [[141, 142, 143, 144], [145, 146, 147, 148]]]]

    print(add_matrices(mat1, mat2))
    print(add_matrices(mat3, mat4))
    print(add_matrices(mat5, mat6))
    print(add_matrices(mat5, mat7))
