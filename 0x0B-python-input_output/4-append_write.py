#!/usr/bin/python3
"""Function that appends a string
    at the end of the text file and returns
    the number of characters added
"""


def append_write(filename="", text=""):
    """Append a text at the end of a file
    and return the number of characteres added

    Args:
        filename (str, optional): text file. Defaults to "".
        text (str, optional): string. Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as writer:
        return writer.write(text)
