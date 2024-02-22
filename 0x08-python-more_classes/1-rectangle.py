#!/usr/bin/python3
""" A module that defines a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""
    def __init__(self, width=0, height=0):
        """instantiatyes an instance with these attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
