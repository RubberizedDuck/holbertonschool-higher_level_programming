#!/usr/bin/python3
""" This module Inherits the Rectangle Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a subclass of Rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ returns the area of a square """
        return self.__size * self.__size
