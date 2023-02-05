#!/usr/bin/python3
""" create a empty class Rectangle """


class Rectangle:
    """ empty field """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """ Private instance attribute: width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """ Private instance attribute: height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
