#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """defines rectangle"""

    def __init__(self, width=0, height=0):
        """properties of the Rectangle"""

        """Initializes instance of rectangle

        Args:
        width(int): width of the rectangle
        height(int): height of the rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width property"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
