#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


""" Module Rectangule that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """ Creats a subclass Rectangle"""

    def __init__(self, width, height):
        """ A constructor that initialises width and heiht"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Implements the area of a rectangle"""

        var = self.__width * self.__height
        return var

    def __str__(self):
        """__str__ method for return the next string"""

        return f"[Rectangle] {self.__width}/{self.__height}"
