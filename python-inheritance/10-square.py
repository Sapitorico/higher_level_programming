#!/usr/bin/python3
""" Write a class Square """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ field to Square """
    def __init__(self, size):
        """ size must be a positive integer """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """ area """
    def area(self):
        return self.__size ** 2
