#!/usr/bin/python3

""" this is a module that checks for inheritance"""

def is_kind_of_class(obj, a_class):
    """ function that checks instance and inheritance"""

    if isinstance(obj, a_class):
        return True
    elif issubclass(object, a_class):
        return True
    else:
        return False
