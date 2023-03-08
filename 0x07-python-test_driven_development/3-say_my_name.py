#!/usr/bin/python3
"""Prints your name"""


def say_my_name(first_name, last_name=""):
    """accepts two arguments

    Args:
    first_name(str): your first name
    last_name(str): your last name"""

    if type(first_name) is not in str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not in str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
