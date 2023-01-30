#!/usr/bin/python3
# access and update private attribute

''' obtain area od square '''


class Square:
    ''' define the initiation'''
    def __init__(self, size=0):
        self.__size = size
        '''create a private attribute '''
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''write a size validation'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        ''' public method thats return area of square'''
        return self.__size**2
