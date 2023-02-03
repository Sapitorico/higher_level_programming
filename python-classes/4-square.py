#!/usr/bin/python3
""" define a square class """


class Square:
    """ create a private instant attribute """
    def __init__(self, size=0):
        self.__size = size

    """ define a Public instance method """
    @property
    def size(self):
        """ size must be an integer size must be >= 0 """
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    """ define a Public instance method """
    @property.setter
    def size(self, value):
        if type(self.__size) is not int:
            raise ValueError("size must be an inter")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ define a Public instance method """
    @property
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("#" * self.__size)