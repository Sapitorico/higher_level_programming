#!/usr/bin/python3
""" define a square class """


class Square:
    """ create a private instant attribute """
    def __init__(self, size=0):
        self.__size = size

    """ define a Public instance method """
    @property
    def size(self):
        return self.__size

    """ define a Public instance method """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ define a Public instance method """
    def area(self):
        return self.__size ** 2
