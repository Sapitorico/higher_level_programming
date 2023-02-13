#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    """ Class constructor: """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    """ Private instance attributes,\
        each with its own public getter and setter: """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
