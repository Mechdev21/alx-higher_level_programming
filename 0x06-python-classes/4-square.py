#!/usr/bin/python3

""" we introduce the concept of setters and getters in our class square"""


class Square:
    """defines atype size"""
    def __init__(self, size=0):
        """initializes size"""
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size**2
        
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """size setter"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

