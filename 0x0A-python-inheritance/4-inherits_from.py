#!/usr/bin/python3
"""
A module containin one function that check nfor the instance
of an object
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    otherwise False.
    Args:
        obj:
        a_class:
    Return:
        True or false
    """
    if type(obj) == a_class:
        return False
    if isinstance(obj, a_class):
        return True
