#!/usr/bin/python3


""" Module of Rectangle that inherits from Rectngle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Creates a subclass Square that inherits from Square"""

    def __init__(self, size):
        """ Constructor that initialises the attributes size"""

        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculates the area of the square"""

        return self.__size**2

    def __str__(self):
        """ implements the string function"""

        return "[Square] {}\{}".format(self.__size, self.__size)
