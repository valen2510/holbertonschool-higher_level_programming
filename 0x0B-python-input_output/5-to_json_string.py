#!/usr/bin/python3
"""function that returns the JSON
    representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """Output JSON object as a string

    Args:
        my_obj (any object python type): python object

    Returns:
        object: JSON object as a string
    """
    return json.dumps(my_obj)
