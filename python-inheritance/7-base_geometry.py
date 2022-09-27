#!/usr/bin/python3
""" This module raises exceptions """


class BaseGeometry:
    """ Class to raise exceptions """
    def area(self):
        """ Exception raised for area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises exceptions if value is not int
        or is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
