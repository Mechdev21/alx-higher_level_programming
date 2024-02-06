#!/usr/bin/python3
""" a class Square that defines a square"""


class Square:
    """creates a model square"""
    def __init__(self, size=0):
        """initializes the attribute size for the
        square instance"""
        self.size = size

    @property
    def size(self):
        """a getter property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of size attribute"""
        if not isinstance(value, int):
            """check to make sure value is an int"""
            raise TypeError("size must be an integer")
        if value < 0:
            """checks tp make sure valueis apositive number"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a quare with #"""
        if self.__size == 0:
            """checks the value of size"""
            print("")
        else:
            """means size is > 0"""
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
