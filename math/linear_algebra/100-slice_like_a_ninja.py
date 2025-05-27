#!/usr/bin/env python3
"""
Function to slice a NumPy matrix along specific axes.
"""

import numpy as np

def np_slice(matrix, axes={}):
    """ Returns a new numpy.ndarray sliced along specified axes. """
    slices = [slice(None)] * matrix.ndim
    for axis, slice_params in axes.items():
        slices[axis] = slice(*slice_params)
    return matrix[tuple(slices)]

if __name__ == '__main__':
    mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                     [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                     [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])

    print(np_slice(mat1, axes={1: (1, 3)}))
    print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
