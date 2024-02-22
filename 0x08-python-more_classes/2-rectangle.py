#!/usr/bin/python3
"""A module that defines a class Rectangle"""


class Rectangle:
    """define a class rectangle"""
    def __init__(self, width=0, height=0):
        """instatiation of an instance with attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """settr method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter property for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """settr method for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimetr of rectangle"""
        if self.__width == 0 or self.__width == 0:
            return 0
        else:
            p = 2 * (self.__width + self.__height)
            return (p)
