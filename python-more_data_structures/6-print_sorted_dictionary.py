#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sortedKeys = sorted(keys)
    for key in sortedKeys:
        print("{}:{}".format(key, a_dictionary[key]))