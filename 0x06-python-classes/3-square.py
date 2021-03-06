#!/usr/bin/python3
"""Square class"""


class Square:
    """Define a Square class"""
    def __init__(self, size=0):
        """Validate size value and initialize Square attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Define Square area"""
        return self.__size ** 2
