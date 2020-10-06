#!/usr/bin/python3
"""function that adds a new
    attribute to an object if
    it’s possible
"""


def add_attribute(att, name, value):
    """Add a new attributes if it's possible"""

    if getattr(att, '__dict__', 1) is 1:
        raise TypeError("can't add new attribute")
    setattr(att, name, value)
