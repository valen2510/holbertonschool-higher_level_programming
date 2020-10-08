#!/usr/bin/python3
""" function that returns the dictionary
    for JSON serialization of an object
"""


def class_to_json(obj):
    """Get the dictionary of a class

    Args:
        obj (class instance): object

    Returns:
        [dict]: object dictionary
    """
    return vars(obj)
