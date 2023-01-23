#!/usr/bin/python3

def no_c(my_string):
    if not my_string:
        return
    return my_string.translate({ord(letter): None for letter in 'c' and 'C'})
