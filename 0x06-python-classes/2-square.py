#!/usr/bin/python3

"""size must be an integer, otherwise raise TypeErro
if size is less than 0, raise a ValueError"""


class Square:
    """defines a type square """
    def __init__(self, size=0):
        """ initialization of attribute size """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
