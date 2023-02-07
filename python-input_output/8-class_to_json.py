#!.usr.bin/python3
""" returns the dictionary description with simple data structure """
import json


def class_to_json(obj):
    """ converts a class to json """
    return obj.__dict__
