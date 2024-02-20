#!/usr/bin/python3
"""
A module with one class and two function:
that creates a class called BaseGeometry
"""


class BaseGeometry:
    """
    This creates a class called BaseGeometry
    that creates instance when called
    """

    def area(self):
        """
        raise an exception when called that area is not
        implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name:str, value):
        """
        a function that validates value and assumes
        name is always astring
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
