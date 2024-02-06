#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """creates a model of a square instance"""
    def __init__(self, size=0):
        """initalization of the size
        attributes in the instance
        Args:
            size: pivate instance
        """
        if type(size) != int:
            """ checks to make sure size
            is an int
            """
            raise TypeError("size must be an integer")
        if size < 0:
            """make sure size is a positive
            number
            """
            raise ValueError("size must be >= 0")
        self.__size = size
