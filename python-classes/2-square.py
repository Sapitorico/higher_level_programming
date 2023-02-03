#!/usr/bin/python3
""" define a square class """


class Square:
    """ create a private instant attribute """
    def __init__(self, size=0):
        self.__size = size
        """ size must be an integer size must be >= 0 """
        if type(size) is not int:
            raise TypeError("ize must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
