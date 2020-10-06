#!/usr/bin/python3
"""class Myint
"""


class MyInt(int):
    """Define a Myint class

    Args:
        int (int): Superclass
    """
    def __init__(self, value):
        """Initialisation

        Args:
            value (int): integer
        """
        self.value = value

    def __eq__(self, other):
        """Comparison using == operator
        """
        return not self.value == other

    def __ne__(self, other):
        """Comparison using != operator
        """
        return not self.value != other
