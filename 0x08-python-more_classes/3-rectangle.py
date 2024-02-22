#!/usr/bin/python3
"""A model of a class that defines Rectangle"""


class Rectangle:
    """defines a class rectangle"""
    def __init__(self, width=0, height=0):
        """imitializes an instance with attributes"""
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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            p = 2 * (self.__width + self.__height)
            return (p)

    def __str__(self):
        """returns a string representation"""
        if self.__width == 0 or self.__height == 0:
            return (" ")
        else:
            rect = ""
            for i in range(self.__height):
                rect += "#" * self.__width + "\n"
            return rect

