#!/usr/bin/python3
"""Function that reads n lines of a text
    file and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file and print it

    Args:
        filename (str, optional): Text file. Defaults to "".
        nb_lines (int, optional): number of lines. Defaults to 0.
    """
    with open(filename, encoding='utf-8') as reader:
        if nb_lines <= 0:
            print(reader.read(), end="")
        else:
            n_lines = 0
            while nb_lines > n_lines:
                print(reader.readline(), end="")
                n_lines += 1
