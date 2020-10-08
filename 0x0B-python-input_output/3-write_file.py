#!/usr/bin/python3
"""Function that writes a string to a text file
    and returns the number of characteres written
"""


def write_file(filename="", text=""):
    """Write a string ina file and return the number of
    characteres

    Args:
        filename (str, optional): text file. Defaults to "".
        text (str, optional): string. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as writer:
        return writer.write(text)
