#!/usr/bin/python3
"""
This module has class Square which inherits from
Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class doc
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ instansiation of parent class Rectangle """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        overrides str method
        """
        method_string = f"[Square] ({self.id}) "
        method_string += f"{self.x}/{self.y} - "
        method_string += f"{self.size}"
        return method_string
