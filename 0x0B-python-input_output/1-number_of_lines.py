#!/usr/bin/python3
"""Function that returns the number
    of lines of a text file
"""


def number_of_lines(filename=""):
    """Return the number of lines of a text
        file

    Args:
        filename (str, optional): text file. Defaults to "".
    """
    with open(filename, encoding='utf-8') as reader:
        return len(reader.readlines())
