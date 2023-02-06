#!/usr/bin/python3
""" subclass Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class field to rectangle """
    def __init__(self, width, height):
        """ width and height must be positive integers,\
            validated by integer_validator """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
