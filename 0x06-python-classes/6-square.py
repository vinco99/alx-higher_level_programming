#!/usr/bin/python3
"""1. Square that accepts size
    contains a class that initializes size
    Contaons a funtion that calculates square
    gats the value of size
    contains a funtion that prints"""

class Square:
    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size and position"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of position."""

        if not isinstance(value, tuple) or \
                len(value) != 2 or not \
                all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area."""

        return self.__size ** 2

    def my_print(self):
        """Prints '#'."""

        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()
