#!/usr/bin/python3
""" write a class Base """


class Base:
    """ define a private attribute """
    __nb_objects = 0
    """ class constructor """
    def __init__(self, id=None):
        """ if id is not None, assign the public instance\
            attribute id with this argument value """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
