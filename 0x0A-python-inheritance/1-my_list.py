#!/usr/bin/python3
""" module with a class list"""
class MyList(list):
    """class mylist is derived from list"""
    pass

    def print_sorted(self):
        """prints list in sorted order"""
        print(sorted(list(self)))
