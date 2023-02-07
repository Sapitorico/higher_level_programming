#!/usr/bin/python3
""" Write a class Student """


class Student:
    """ Public instance attributes: """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Public method  """
    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
