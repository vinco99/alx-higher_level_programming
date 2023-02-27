#!/usr/bin/python3
"""1. Square that accepts size
    contains a class that initialize size
    contains a function that calculates area."""

class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initializes size of Square."""

        self.size = size

    @property
    def size(self):
        """Gets size of square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size."""

        if not isinstance(value, int) :
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area."""

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""

        if self.__size == 0:
            print()
            return
        for _ in range(self.size):
            for _ in range(self.size):
                print('#', end="")
            print()

