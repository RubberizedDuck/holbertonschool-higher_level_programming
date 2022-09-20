#!/usr/bin/python3
""" class for rectangle """


class Rectangle:
    """ rectangle class """
    def __init__(self, width=0, height=0):
        """
        runs a check to ensure that width & height are
        integer values and not less than 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def __str__(self):
        """
        returns the string representation of the class
        using # as the symbol for row and column
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            for column in range(self.__width):
                string += "#"
            if row != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        return a string representation of class
        in a new instance
        """
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    @property
    def width(self):
        """
        returns the private variable width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the private variable of width
        and checks type and value are correct
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns the private variable height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the private variable of height &
        checks that size is the correct type and value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
