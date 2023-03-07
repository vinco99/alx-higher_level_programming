#!/usr/bin/python3
"""A Rectangle class that has width and height"""

class Rectangle:
    """Initializes the properties of the rectangle"""

    def __init__(self, width=0, height=0):
        """initializes the width and height

        Args:
        width(int): the rectangle width
        height(int): the rectangle height"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width"""

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
        """Gets the hieght"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the Area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the Perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)
