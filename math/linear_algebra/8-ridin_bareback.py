#!/usr/bin/env python3
"""
Function to perform matrix multiplication.
"""

def mat_mul(mat1, mat2):
    """ Returns the matrix multiplication of mat1 and mat2, or None if they cannot be multiplied. """
    if len(mat1[0]) != len(mat2):  # Check if matrices can be multiplied
        return None
    
    # Compute matrix multiplication using list comprehension
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]

# Example Usage:
if __name__ == '__main__':
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]

    print(mat_mul(mat1, mat2))  # Expected Output: [[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]
