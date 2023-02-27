#!/usr/bin/python3
"""1. Square that accepts size
    Initializes size
    contains a function thst calculates the square
    can access the value of declared size."""

class Square:
    """A Square class"""

    def __init__(self, size=0):
        """Initializes the size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square."""

        return self.__size ** 2
