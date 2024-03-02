#!/usr/bin/python3
"""Prints a string"""


def text_indentation(text):
    """Prints a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = [".", ",", "?", ":"]
    for delim in i:
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])
    print(text, end="")
