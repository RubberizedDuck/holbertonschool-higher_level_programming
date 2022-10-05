#!/usr/bin/python3
"""
This module contains Rectangle which inherits
from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class docs go here. Will add later
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instansiation of class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """
        prints size of rectangle
        including the x and y axis
        """
        for y_axis in range(self.y):
            print()
        for row in range(self.height):
            for x_axis in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        updates variables for passed arguments
        """
        if args is not None and len(args) > 0:
            for argv, arg in enumerate(args):
                if argv == 0:
                    self.id = arg
                if argv == 1:
                    self.width = arg
                if argv == 2:
                    self.height = arg
                if argv == 3:
                    self.x = arg
                if argv == 4:
                    self.y = arg
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        """ changing the string method """
        method_string = f"[Rectangle] ({self.id}) "
        method_string += f"{self.x}/{self.y} - "
        method_string += f"{self.width}/{self.height}"
        return method_string

    @property
    def width(self):
        """ getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of height """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of x """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y """
        self.validator("y", value)
        self.__y = value

    def validator(self, attribute, value):
        """
        validator to make sure function
        is being used correctly
        """
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute == "width" or attribute == "height":
            if value <= 0:
                raise ValueError(f"{attribute} must be > 0")
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")

    def to_dictionary(self):
        """ returns the dictionary rep of Rectangle """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
