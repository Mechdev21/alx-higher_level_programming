#!/usr/bin/python3
"""A module for Rectangle"""


class Rectangle:
    """Creates a class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialise the width and height"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """returns the height value"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the value of hright"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """returns the width value"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the string represemtation"""
        total = ""
        for i in range(self.__height):
            for j in range(self.__width):
                total += '#'
            if self.__width != 0 and i < (self.__height - 1):
                total += '\n'
        return total

    def __repr__(self):
        """returns a representstion oof object"""
        return ("Rectangle({:d},{:d})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instace"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
