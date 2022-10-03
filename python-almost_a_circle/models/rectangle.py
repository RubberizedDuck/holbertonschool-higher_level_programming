#!/usr/bin/python3
"""
This module contains Rectangle which inherits
from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class docs go here. Will add later
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ prints size of rectangle """
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ changing the string method """
        method_string = f"[Rectangle] ({self.id}) "
        method_string += f"{self.x}/{self.y} - "
        method_string += f"{self.width}/{self.height}"
        return method_string

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def validator(self, attribute, value):
        """
        validator to make sure function
        is being used correctly
        """
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute == "width" or attribute == "height":
            if value <= 0:
                raise ValueError(f"{attribute} must be > 0")
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
