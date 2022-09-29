#!/usr/bin/python3
"""
Module to add attribute to compatible classes or objects
"""


def add_attribute(obj, name, value):
    """
    checks data, if object is compatiable, adds attr
    to class
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
