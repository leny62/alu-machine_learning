#!/usr/bin/env python3
"""
Function to concatenate two matrices (nested lists) along a specified axis.
If the matrices cannot be concatenated, return None.
"""

def cat_matrices(mat1, mat2, axis=0):
    # Helper function that returns the shape of a nested list.
    def shape(matrix):
        if not isinstance(matrix, list):
            return []
        return [len(matrix)] + shape(matrix[0])
    
    s1, s2 = shape(mat1), shape(mat2)
    
    if axis == 0:
        # For axis 0, the dimensions beyond the first must be identical.
        if s1[1:] != s2[1:]:
            return None
        # Concatenation along axis 0 is simple list concatenation.
        return mat1 + mat2
    else:
        # For concatenation along a deeper axis, the top-level dimensions must match.
        if s1[0] != s2[0]:
            return None
        result = []
        for i in range(len(mat1)):
            # Recursively concatenate along (axis - 1) for each corresponding element.
            sub = cat_matrices(mat1[i], mat2[i], axis=axis-1)
            if sub is None:
                return None
            result.append(sub)
        return result
