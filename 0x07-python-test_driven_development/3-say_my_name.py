#!/usr/bin/python3
""" this is a module that prints my name"""


def say_my_name(first_name, last_name=""):
    """ function prints my name
    it take two string arguments
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
