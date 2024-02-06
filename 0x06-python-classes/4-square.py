#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """create a model of instances of a square"""
    def __init__(self, size):
        """iniatializattion of the intance attribute
        Args:
            size: private instance attribute
        """
        self.size = size

    @property
    def size(self):
        """returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """resets the value of size"""
        if not isinstance(value, int):
            """checks to be sure type is an int"""
            raise TypeError("size must be an integer")
        if value < 0:
            """checks to make sure size is not negative"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)
