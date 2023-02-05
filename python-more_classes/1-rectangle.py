#!/usr/bin/python3
""" create a empty class Rectangle """


class Rectangle:
    """ empty field """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """ Private instance attribute: width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width must be an integer """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """ if width is less than 0 """
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Private instance attribute: height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height must be an integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """ if height is less than 0 """
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
