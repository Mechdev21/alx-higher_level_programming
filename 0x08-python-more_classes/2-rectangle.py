#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """Creates a class Rectangle"""

    def __init__(self, width=0, height=0):
        """init method"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter def"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter def"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area"""
        rec_area = self.__width * self.__height
        return rec_area

    def perimeter(self):
        """checks the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        per = (self.width + self.__width) + (self.__height + self.__height)
        return per
