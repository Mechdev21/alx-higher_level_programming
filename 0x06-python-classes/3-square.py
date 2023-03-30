#!/usr/bin/python3

""" write a class square 
Public instance method: def area(self): that returns the current square area"""


class Square:
    """ defines a type square """
    def __init__(self, size=0):
        """initializes the size """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """ returs the area of the square """
        dArea = self.__size * self.__size
        return dArea
