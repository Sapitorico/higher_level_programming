#!/usr/bin/python3
""" module for defiing the basegeo class """


class BaseGeometry:
    """ class has area and integer methods """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")