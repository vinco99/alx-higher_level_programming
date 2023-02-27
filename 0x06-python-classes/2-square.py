#!/usr/bin/python3
"""3. A Square class with size validation
    contains private intance attribute size
    calculates the area of the square."""

class Square:
    """A Square class."""

    def __init__(self, size=0):
        """initialize class with size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
