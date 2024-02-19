#!/usr/bin/python3
"""
this module contain pone funcion that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns TRUE if the object is an instance of
    or the objected is an instance of a class that is inherited from
    Aregs:
        obj:
        a_class:
    Returns:
        Treue or False
    """
    return isinstance(obj, a_class)
