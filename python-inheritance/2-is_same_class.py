#!/usr/bin/python3
""" write a function that return true or false\
    f the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ return false or true """
    if isinstance(type(obj), type(a_class)):
        return True
    else:
        return False
