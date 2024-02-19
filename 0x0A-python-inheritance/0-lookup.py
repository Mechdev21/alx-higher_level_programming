#!/usr/bin/python3
""" This module contain one function that returns a
list of attributes and method"""


def lookup(obj):
    """
    A function that returns a list of attributes
    and method
    Args:
        obj
    Returns:
        list of obj attributes and method
    """
    return (dir(obj))
