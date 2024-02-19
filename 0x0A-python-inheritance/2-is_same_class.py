#!/usr/bin/python3
"""A module that has one function tjhat
checks if an obj is an instace of a class"""


def is_same_class(obj, a_class):
    """
    a function that checks for the class of
    the object
    Args:
        obj
        a_class
    Return:
        True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
