#!/usr/bin/python3
""" write a class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ doc """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ doc """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
