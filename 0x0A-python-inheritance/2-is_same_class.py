#!/usr/bin/python3
"""Function to returns True it he object
    if the object is the exact instance
    or False
"""


def is_same_class(obj, a_class):
    """Return if an object is an instance
    of the class
    """

    return type(obj) is a_class
