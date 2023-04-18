#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """creates a new class Rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor for height and width"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
