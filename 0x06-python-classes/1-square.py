#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Creates a new class square
    Args:
        None
    Return:
        None
    """
    def __init__(self, size):
        """initialises the class instance
        Args:
            _size: a private instance attribute
        Return:
            None
        """
        self.__size = size #: size of the square
