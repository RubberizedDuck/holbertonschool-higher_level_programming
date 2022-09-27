#!/usr/bin/python3
"""
This module checks if the object is
from the same class
"""


def is_same_class(obj, a_class):
    """
    Returns True or False depending if
    the class is the same as object passed
    """
    return type(obj) is a_class
