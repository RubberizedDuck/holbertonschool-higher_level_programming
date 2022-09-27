#!/usr/bin/python3
""" This module inherits BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle is subclass of BaseGeometry """

    def __init__(self, width, height):
        """ init for Rectangle, using inherited integer_validator """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns area of width and height """
        return self.__width * self.__height

    def __str__(self):
        """ changes return of string """
        return f"[Rectangle] {self.__width}/{self.__height}"
