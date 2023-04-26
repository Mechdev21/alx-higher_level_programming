#!/usr/bin/python3
"""A module of Rectangle class"""


class Rectangle:
    """Creates a new class"""
    def __init__(self, width=0, height=0):
        """Initialise Width and height"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """returns the height value"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ returns width value"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValuaError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        R_per = (self.__width + self.__width) + (self.__height + self.__height)
        return R_per

    def __str__(self):
        """returns string representation"""
        total = ""
        for i in range(self.__height):
            for j in range(self.__width):
                total += '#'
            if self.__width != 0 and i < (self.__height - 1):
                total += '\n'
        return total

    def __repr__(self):
        """returms representation of the objext"""
        return ("Rectangle({:d},{:d})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")

