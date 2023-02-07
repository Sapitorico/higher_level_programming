#!/usr/bin/python3
""" function that return the json representation and (string)"""
import json


def to_json_string(my_obj):
    """ representation of an objet """
    return json.dumps(my_obj)
