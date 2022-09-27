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
