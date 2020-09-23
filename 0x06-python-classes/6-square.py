#!/usr/bin/python3
"""Square class"""


class Square:
    """Define Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Validate size value and initialize Square attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
        if type(position) is not tuple or position[0] < 0 or position[1] < 0\
            or type(position[0]) is not int or type(position[1]) is not int\
                or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    @property
    def size(self):
        """Get size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size value"""
        self.__size = value

    @property
    def position(self):
        """Get position values"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set tuple value"""
        self.__position = value

    def area(self):
        """Define Square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the Square with #"""
        if self.__size == 0:
            print("")
        if self.__position[1] >= 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
