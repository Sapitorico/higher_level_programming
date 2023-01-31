#!/usr/bin/python3
''' create a class square '''


class Square:
    ''' define the initiation'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        ''' public method thats return position of square'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
            not all(isinstance(num, int) for num in value) or\
            not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        ''' public method thats return area of square'''
        return self.__size**2

    ''' print a square of # the size of self.__size'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                if i+1 < self.__size:
                    print()
            print()
