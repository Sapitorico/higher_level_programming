#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    """ Class constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """ Call the super class with id """
        super().__init__(id)
