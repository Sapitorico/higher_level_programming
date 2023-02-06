#!/usr/bin/python3
""" Write a class MyList """


class MyList(list):
    """ Public instance method print sorted """
    def print_sorted(self):
        print(sorted(self))
