#!/usr/bin/python3
"""
This module contains 1 class
Studen
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ instantiation for class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dictionary representation of the class
        """
        if type(attrs) is list:
            for var in attrs:
                if type(var) != str:
                    return self.__dict__
            return {var: self.__dict__[var] for var in attrs
                    if hasattr(self, var)}
        else:
            return self.__dict__
