#!/usr/bin/python3
""" define a function that adds aa two integers or float """


def add_integer(a, b=98):
    """ a and b must be integers or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    """ return to result """
    return a + b
