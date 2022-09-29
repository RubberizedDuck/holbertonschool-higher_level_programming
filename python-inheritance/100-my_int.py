#!/usr/bin/python3
"""
This module has the rebel class MyInt
"""


class MyInt(int):
    """
    Reversing the == and != operators
    """
    def __eq__(self, other):
        """
        Reverses the == operator
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Reverses the != operator
        """
        return int(self) == other
