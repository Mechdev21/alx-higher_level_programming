#!/usr/bin/python3
"""
a function that adds two nambers
"""


def add_integer(a, b=98):
    """this functions try to add two int
    Args:
        a, b
    Returns:
        the sum
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
