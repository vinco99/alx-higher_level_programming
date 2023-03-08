#!/usr/bin/python3
"""prints '#' n times"""

def print_square(size):
    """accepts an argument size"""

    if is not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
