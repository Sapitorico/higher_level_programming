#!/usr/bin/python3
""" function that append a string in the end of the file"""


def append_write(filename="", text=""):
    """ function that append a string in the end of the file"""
    with open(filename, "a") as f:
        return f.write(text)
