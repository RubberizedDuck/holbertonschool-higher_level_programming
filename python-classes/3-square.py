#!/usr/bin/python3
"""defines class Square"""


class Square:
    """class for Square"""
    def __init__(self, size=0):
        """
        runs a check to ensure that size is integer value
        and that it is not less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the area size of the square
        """
        return self.__size * self.__size
