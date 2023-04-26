#!/usr/bin/python3
""" A module of Rectangle class"""


class Rectangle:
   """ Creates a Rectangle class"""
   number_of_instances = 0
   print_symbol = '#'

   def __init__(self, width=0, height=0):
       """Initialisez width and height"""
       self.__width = width
       self.__height = height
       type(self).number_of_instances += 1

   @property
   def width(self):
       """returns width vslue"""
       return self.__width
   @width.setter
   def width(self, value):
       """Sets the value of width"""
       if not isinstance(value, int):
           raise TypeError("width must be an integer")
       if value < 0:
           raise ValueError("width must be >= 0")
       self.__width = value

   @property
   def height(self):
       """return height value"""
       return self.__height
   @height.setter
   def height(self, value):
       """Sets the value of height"""
       if not isinstance(value, int):
           raise TypeError("height must be an integer")
       if value < 0:
           raise ValueError("height must be >= 0")
       self.__height = value

   def area(self):
       """calculates the area"""
       return self.__width * self.__height

   def perimeter(self):
       """calculates the perimeter"""
       if self.__width == 0 or self.__height == 0:
           return 0
       return ((self.__width * 2) + (self.__height * 2))

   def __str__(self):
       """rwturns the string representation"""
       total = ""
       for i in range(self.__height):
           for j in range(self.__width):
               total += "{}".format(self.print_symbol)
           if self.__width != 0 and i < (self.__height - 1):
               total += '\n'
       return total

   def __repr__(self):
       """returns a rep ofvthe object"""
       return ("Rectangle ({:d},{:d})".format(self.__width, self.__height))

   def __del__(self):
       """ deletes an instance"""
       type(self).number_of_instances -= 1
       print("Bye rectangle...")
