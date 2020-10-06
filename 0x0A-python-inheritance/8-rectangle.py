#!/usr/bin/python3
"""class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class Rectangle

    Args:
        BaseGeometry (BaseGeometry): superclass
    """
    def __init__(self, width, height):
        """Initialisation of class Rectangle

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
