#!/usr/bin/python3
"""
This is a 0_add_integer module
It has a funtion def add_integer(a, b=98):
"""


def add_integer(a, b=98):
    """Return the sum of two numbers a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
