#!/usr/bin/python3


""" Module that chercks for inheritance directly or indirectly"""


def inherits_from(obj, a_class):

    """ function that returns true if its an instance of a
    class vor inherits from another class"""

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
