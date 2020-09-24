#!/usr/bin/python3
"""MagicClass class"""


class MagicClass:
    """Define Magicclass"""

    def __init__(self, radius):
        """Initialize and validate attributes"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Define method area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """define method circumference"""
        return 2 * math.pi * self._MagicClass__radius
