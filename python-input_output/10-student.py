#!/usr/bin/python3
""" Write a class Student """


class Student:
    """ Public instance attributes: """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Public method  """
    def to_json(self, attrs=None):
        """ only attribute names contained in this list must be retrieved\
            Otherwise, all attributes must be retrieved """
        if attrs is None:
            attrs = ["first_name", "last_name", "age"]
        attrs.append(self.age)
        attrs.append(self.first_name)
        attrs.append(self.last_name)
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
