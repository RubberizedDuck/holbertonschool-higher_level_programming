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

    def to_json(self):
        """
        returns dictionary representation of the class
        """
        return self.__dict__
