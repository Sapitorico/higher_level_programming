#!/usr/bin/python3
''' define a class Squares '''


class Square:
    ''' define the initiation'''
    def __init__(self, size=0):
        '''create a private attribute '''
        self.__size = size
        '''write a size validation'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")