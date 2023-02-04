#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """size must be an integer """
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    """print square"""
    for i in range(size):
        print('#' * size)
