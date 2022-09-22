#!/usr/bin/python3
"""
This module is designed to use 1 function:
say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints "My name is <first_name> <last_name>"
    Raises TypeError if <first_name> or <last_name> aren't a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
