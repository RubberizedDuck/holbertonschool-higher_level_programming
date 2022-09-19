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

    @property
    def size(self):
        """
        Returns the privately stored variable size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the private variable of size &
        checks that size is the correct type and value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        """
        if self.__size == 0:
            print()
        for length in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print()
