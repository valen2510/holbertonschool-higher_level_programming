#!/usr/bin/python3
"""Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id (int, optional): Rectangle identification. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter

        Returns:
            int: private instance attribute width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Height Getter

        Returns:
            int: private instance attribute height of rectangle
        """
        return self.__height

    @property
    def x(self):
        """x Getter

        Returns:
            int: private instance attribute x of rectangle
        """
        return self.__x

    @property
    def y(self):
        """y Getter

        Returns:
            int: private instance attribute y of rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Define Rectangle area

        Returns:
            int : Rectangle area value
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with character #
        """
        [print("") for _ in range(self.__y)]
        [print(" " * self.x + "#" * self.width) for _ in range(self.height)]

    def __str__(self):
        """String representation of Rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the value of the Rectangle with arbitrary
        arguments or keyword arguments
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and args[0] is not None:
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """dictionary representation of a Rectangle

        Returns:
            dict: attribute dictionary of Rectangle
        """
        new_dict = {'id': self.id, 'width': self.width, 'height': self.height,
                    'x': self.x, 'y': self.y}
        return new_dict
