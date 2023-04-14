#!/usr/bin/python3


""" Module of function that set attributes"""


def add_attribute(obj, name, value):
    """ Functions that sets new attributes"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
