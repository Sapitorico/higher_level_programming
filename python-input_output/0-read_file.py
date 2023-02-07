#!/usr/bin/python3
""" write a function that read a text file"""


def read_file(self):
    """ must use the with """
    with open(self, 'r') as f:
        [print(line, end="") for line in f.readlines()]
