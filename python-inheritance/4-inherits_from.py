#!/usr/bin/python3
""" check if the object is an instance of a class """


def inherits_from(obj, a_class):
    """ check if the object
    is an instance of a class """
    return type(obj) is not a_class
