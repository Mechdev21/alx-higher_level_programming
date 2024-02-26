#!/usr/bin/python3
"""A module that defines a type square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """DEfines a class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of the object attributes"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """returns the string representation"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """seter meyhid for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """updates the attribute of an instace"""
        att = [self.id, self.__size, self.x, self.y]
        for i, j in enumerate(args):
            att[i] = j
        self.id, self.__size, self.x, self.y = att
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self.__dict__

    def to_dictionary(self):
        """returns the dict repr"""
        return self.__dict__
