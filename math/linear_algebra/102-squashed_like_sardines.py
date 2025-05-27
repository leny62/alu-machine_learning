#!/usr/bin/env python3
"""
Function to concatenate two matrices (nested lists) along a specified axis.
If the matrices cannot be concatenated, return None.
"""

def cat_matrices(mat1, mat2, axis=0):
    def shape(matrix):
        if not isinstance(matrix, list):
            return []
        return [len(matrix)] + shape(matrix[0])
    
    s1, s2 = shape(mat1), shape(mat2)
    
    if axis == 0:
        if s1[1:] != s2[1:]:
            return None
        return mat1 + mat2
    else:
        if s1[0] != s2[0]:
            return None
        result = []
        for i in range(len(mat1)):
            sub = cat_matrices(mat1[i], mat2[i], axis=axis-1)
            if sub is None:
                return None
            result.append(sub)
        return result
