#!/usr/bin/python3
''' define a class Squares '''


class Square:
    def __init__(self, size=0):
		''' write a size validation '''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
