#!/usr/bin/python3
""" Class Mylist that inherits
    from list
"""


class MyList(list):
    """Define Myclass subclass

    Args:
        list (list): class list
    """
    def print_sorted(self):
        """Prints the list sorted
        """
        print(sorted(self))
