#!/usr/bin/python3
""" function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ first_name and last_name must be strings otherwise """
    if not isinstance(first_name, str):
        raise TypeError("First and last names must be strings")
    if not isinstance(last_name, str):
        raise TypeError("Last and first names must be strings")
    print(f"My name is {first_name} {last_name}")