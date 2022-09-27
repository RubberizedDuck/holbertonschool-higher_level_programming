#!/usr/bin/python3
"""
This module contains one function that returns
a list format of every attribute and method
of an object
"""


def lookup(obj):
    """
    Takes the object and returns a list of attributes
    and methods within that object
    """
    return dir(obj)
