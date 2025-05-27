#!/usr/bin/env python3
"""
Function to perform element-wise arithmetic operations on NumPy arrays.
"""

import numpy as np

def np_elementwise(mat1, mat2):
    """ Returns a tuple containing element-wise sum, difference, product, and quotient. """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

if __name__ == '__main__':
    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6]])

    add, sub, mul, div = np_elementwise(mat1, mat2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

    add, sub, mul, div = np_elementwise(mat1, 2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
