#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


""" Module of a Square class inheriting from Rectangle"""


class Square(Rectangle):
    """ Creates a subclass Square from Rectangle"""

    def __init__(self, size):
        """ Constructor that initialises size"""

        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculates the area of the square"""

        return self.__size**2
