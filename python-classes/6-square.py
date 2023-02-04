#!/usr/bin/python3
""" define a square class """


class Square:
    """ create a private instant attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    """ define a Public instance method """
    @property
    def size(self):
        return self.__size

    """ define a Public instance method """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an inter")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ define a Public instance method """
    @property
    def position(self):
        return self.__position

    """ define a Public instance method """
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a \
tuple of 2 positive integers")
        self.__position = value

    """ define a Public instance method """
    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
