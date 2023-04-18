#!/usr/bin/python3


""" Module Rectangle that inherits from basegeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class rectangle that inhedrits from basegeometry"""


    def __init__(self, width, height):
        """ Aconstructor that that instantiates attributes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
