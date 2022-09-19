#!/usr/bin/python3
"""defines class Square"""


class Square:
    """class for Square"""
    def __init__(self, size=0, position=(0, 0)):
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

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """ returns the privately stored variable position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the private variable of position &
        checks if position is a tuple and if what is stored
        in the tuple are integers
        """
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """
        prints size of square to stdout
        takes into account position tuple
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for length in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for width in range(self.__size):
                print("#", end="")
            print()
