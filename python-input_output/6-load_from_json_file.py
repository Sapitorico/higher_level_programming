#!/usr/bin/python3
""" function that creates an Object from a “JSON file”: """
import json


def load_from_json_file(filename):
    """ must use the with statement """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
