#!/usr/bin/python3
"""function that creates an
    Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """Creates an object froma a JSON file

    Args:
        filename (JSON): JSON file

    Returns:
        object: python object
    """
    with open(filename, encoding="utf-8") as reader:
        return json.load(reader)
