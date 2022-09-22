#!/usr/bin/python3
"""
checks if a & b are type of int or float
if a or b equals a float, converts them to an int
then returns value of a + b
"""


def add_integer(a, b=98):
    """
    returns the value of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
