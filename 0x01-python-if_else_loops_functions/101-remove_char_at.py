#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) >= n and n >= 0:
        copy = str[:n] + str[n + 1:]
    else:
        copy = str
    return copy
