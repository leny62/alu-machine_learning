#!/usr/bin/env python3

"""
Function to func 1 trim me down.
"""


import numpy as np

matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = [row[2:4] for row in matrix]  # Extract columns 3 and 4

print("The middle columns of the matrix are: {}".format(the_middle))

if __name__ == "__main__":
    func_1_trim_me_down()
