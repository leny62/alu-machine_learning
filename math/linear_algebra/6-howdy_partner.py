#!/usr/bin/env python3
"""
Function to concatenate two arrays.
"""

def cat_arrays(arr1, arr2):
    """ Returns a new list by concatenating arr1 and arr2. """
    return arr1 + arr2  # Concatenates the two lists

# Example Usage:
if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]

    print(cat_arrays(arr1, arr2))  # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
    print(arr1)  # Original list remains unchanged: [1, 2, 3, 4, 5]
    print(arr2)  # Original list remains unchanged: [6, 7, 8]
