#!/usr/bin/python3
"""function that returns an object
    (Python data structure) represented
    by a JSON string
"""


import json


def from_json_string(my_str):
    """Load JSON data from a string to
    retrieve a Python object

    Args:
        my_str (str): string representation in JSON

    Returns:
        object: Pyhton object
    """
    return json.loads(my_str)
