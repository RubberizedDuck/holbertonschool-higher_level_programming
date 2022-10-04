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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ allows updating of variables with kwargs and args """
        if args is not None and len(args) > 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
