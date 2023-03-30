#!/usr/bin/python3

""" add a functionality thats lets us print a square in our class
Public instance method: def my_print(self)"""


class Square:
    """defines a type square"""
    def __init__(self, size=0):
        """initialises size"""
        self.__size = size
    def area(self):
        """returns area of the square"""
        return self.__size**2
    def my_print(self):
        """prints a square"""
        if self.__size == 0:
             print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end = "")
                print()
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

