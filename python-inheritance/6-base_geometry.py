#!/usr/bin/python3
""" This module raises an exception """


class BaseGeometry:
    """ Class to raise exceptions """
    def area(self):
        """ Exception raised for area """
        raise Exception("area() is not implemented")
