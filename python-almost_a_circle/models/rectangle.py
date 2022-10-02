#!/usr/bin/python3
"""
This module contains Rectangle which inherits
from the Base class
"""
from base import Base


class Rectangle(Base):
    """
    Class docs go here. Will add later
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self):
        pass

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        self.height = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self):
        self.width = x
