#!/usr/bin/python3
""" check if the object is an instance of a class """


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class """
    if type(obj) is float and type(obj) is None:
        return False
    return type(obj) is not a_class