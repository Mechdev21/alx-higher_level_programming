#!/usr/bin/python3
"""A model that defines a class Rectangle"""


class Rectangle:
    """Defines aclass Rectangle"""
    def __init__(self, width=0, height=0):
        """instatiation of the instance attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines the width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """width getter method"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """defines the height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the arae of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            p = 2 * (self.__width + self.__height)
            return p

    def __str__(self):
        """the magic method str"""
        shape = ""
        for i in range(self.__height):
            for j in range(self.__width):
                shape += "#"
            if self.__width != 0 and i < (self.__height - 1):
                shape += "\n"
        return shape

    def __repr__(self):
        """representation of tghe rectangle"""
        return ("Rectangle({},{})".format(self.__width, self.__height))
