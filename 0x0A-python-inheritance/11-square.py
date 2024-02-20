#!/usr/bin/python3
"""A module that creates a class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates a new class square from rectangle"""
    
    def __init__(self, size):
        """initalization of instance variable size"""
        self.integer_validator("size", size)
        self.__size = size
        
    def area(self):
        """implements the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """implentation of the magic method to print"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
