#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Creates a  model of the square instance"""
    def __init__(self, size=0):
        """initialization of the class object attributes
        Args:
            size: a private instace attribute
        """
        if not isinstance(size, int):
            """checks to make sure size is an int"""
            raise TypeError("size must be an integer")
        if size < 0:
            """checks to make sure size is a positive int"""
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return (self.__size * self.__size)
