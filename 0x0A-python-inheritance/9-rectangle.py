#!/usr/bin/python3
"""A module class called Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a class called Rectangle"""

    def __init__(self, width, height):
        """width and height are private instance initialization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implements the area of a rectangle"""
        return self.__height * self.__width
    def __str__(self):
        """implemeents the magic function print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
