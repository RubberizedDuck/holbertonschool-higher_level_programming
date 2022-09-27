#!/usr/bin/python3
"""
This module is designed to take in the super class list
as a parameter and sort that list that is given
"""


class MyList(list):
    """
    This class inherits from the super class list
    and prints out a sorted list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        This method prints a sorted list
        """
        print(sorted(self))
