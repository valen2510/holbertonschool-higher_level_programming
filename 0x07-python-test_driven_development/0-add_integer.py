#!/usr/bin/python3
"""
Function to add two integers,a and b,
they must be integers or floats, otherwise
raise a TypeError exception
"""


def add_integer(a, b=98):
    """ Add two integers (a and b)
    a and b should be int or float type
    return int addition """

    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is float or type(b) is int:
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return int(a + b)
