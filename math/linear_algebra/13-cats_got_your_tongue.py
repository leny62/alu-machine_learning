#!/usr/bin/env python3
"""
Function to concatenate two NumPy matrices along a specific axis.
"""

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """ Returns a new numpy.ndarray by concatenating mat1 and mat2 along the given axis. """
    return np.concatenate((mat1, mat2), axis=axis)

if __name__ == '__main__':
    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6]])
    mat3 = np.array([[7], [8]])

    print(np_cat(mat1, mat2))
    print(np_cat(mat1, mat2, axis=1))
    print(np_cat(mat1, mat3, axis=1))
