#!/usr/bin/python3
"""
Module containts a locked class that only
first_name can be used dynamically
"""


class LockedClass:
    """
    slots locks the class to only let the user
    dynamically create the instance attribute 'first_name'
    """
    __slots__ = ["first_name"]
