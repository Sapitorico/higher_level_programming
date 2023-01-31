#!/usr/bin/python3
''' create a class square '''


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

    ''' print a square of # the size of self.__size'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.__size):
                print()
                for j in range(self.__size):
                    print('#', end="")
            print()
