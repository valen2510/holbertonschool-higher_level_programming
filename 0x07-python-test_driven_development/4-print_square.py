#!/usr/bin/python3
"""Function to print a square
    with the character #. size must be
    0 or a positive integer, otherwise raise a
    ValueError or TypeError.
"""


def print_square(size):
    """Print a square with # character and size 0 or
    a positive integer, otherwise raise exceptions.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
