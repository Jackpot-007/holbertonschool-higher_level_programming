#!/usr/bin/python3
"""Define a function that returns the list of available\
    attributes and methods of an object:
"""


def lookup(obj):
    """Function that returns the list of available attributes and methods\
        f an object
    """
    return dir(obj)
