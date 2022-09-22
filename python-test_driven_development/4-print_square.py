#!/usr/bin/python3
"""
This module is designed to supply 1 function:
print_square
"""


def print_square(size):
    """
    Function that prints a square with the character #
    by using size as the size of the square
    raises TypeError if size is not an integer number
    raises ValueError if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
