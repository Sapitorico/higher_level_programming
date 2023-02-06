#!/usr/bin/python3
""" Write an empty class BaseGeometry. """


class BaseGeometry:
    """ Public instance method """
    def area(self):
        raise Exception("area() is not implemented")

    """ Public instance method """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
