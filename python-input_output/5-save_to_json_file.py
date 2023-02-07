#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation: """
import json


def save_to_json_file(my_obj, filename):
    """ must use the with statement """
    json_file = json.dumps(my_obj)
    with open(filename, 'w') as outfile:
        outfile.write(json_file)
