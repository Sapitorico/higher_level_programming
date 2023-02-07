#!/usr/bin/python3
""" Write a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ must use the with """
    with open(filename, 'w') as f:
        return f.write(text)
