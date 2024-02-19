#!/usr/bin/python3
"""a module that contains a class that inherits from list
and a function that sorts it"""


class MyList(list):
    """
    A child class Mylist is created and it inherits from the
    parent class list"""

    def print_sorted(self):
        """
        sort the list in ascending order
        """
        print(sorted(self))
