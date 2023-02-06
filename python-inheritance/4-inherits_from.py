#!/usr/bin/python3
""" check if the object is an instance of a class """


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class """
    if obj is None and a_class is object:
        return True
    elif type(obj) is float or obj is None:
        return False
    return type(obj) is not a_class
