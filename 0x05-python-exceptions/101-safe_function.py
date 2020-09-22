#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(args[0], args[1])
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return None
