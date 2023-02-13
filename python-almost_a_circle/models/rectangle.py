#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    __width = 0
    __height = 0
    __x = 0
    __y = 0
    """ Class constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes """
        __width = width
        __height = height
        __x = x
        __y = y
        """ Call the super class with id """
        super().__init__(id)