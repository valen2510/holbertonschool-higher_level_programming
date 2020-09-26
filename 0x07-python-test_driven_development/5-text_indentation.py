#!/usr/bin/python3
"""Function that prints a text with two lines
    after enconters the characteres '.' '?' and ':'.
    The text must be a string and the lines printed
    should have extra spaces
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_new = text.replace('.', ".\n\n").replace('?', "?\n\n")\
        .replace(':', ":\n\n")
    for ch in range(len(text_new)):
        if text_new[ch] == ' ' and text_new[ch - 1] == '\n':
            continue
        if ch < len(text_new):
            print("{}".format(text_new[ch]), end="")
        else:
            print("{}".format(text_new[ch]), end="")
