#!/usr/bin/python3


""" A module of MyInt class"""


class MyInt(int):
    """craetes a new class Myint a subclass of int"""

    def __init__(self, value):
        """ A init method that initialises value"""

        self.__value = value

    @property
    def value(self):
        """returns the value """

        return self.__value

    @value.setter
    def value(self, value):
        """ a setter method for value"""

        if type(value) != int:
            raise TypeError("Value must be an int")
        if value <= 0:
            raise ValueError("value must be greater than 0")
        else:
            self.__value = value

    def __eq__(self, other):
        """ checks for == of two instance"""

        if self.__value == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """ checks for != of two instance"""

        if self.__value != other:
            return True
        else:
            return True
