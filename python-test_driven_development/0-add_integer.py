#!/usr/bin/python3
""" create a function that adds 2 integers """


def add_integer(a, b=98):
    """ a and b must be to integer or float """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    """ the result it must be returned inter"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
