#!/usr/bin/python3

""" Module of class BaseGeometry"""

class BaseGeometry:

    """creates a class basegeometry"""

    def area(self):

        """raise an exception error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """validates the value"""

        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.name = name
            self.value = value
