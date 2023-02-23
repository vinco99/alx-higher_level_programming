#!/usr/bin/python3

"""1. Square class
    contains size validation
    contains a function for calculating the area."""
class Square:
    """A Square class that accepts size."""

    def __init__(self, size=0):
        """Size initialization."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area."""

        return self.__size ** 2
