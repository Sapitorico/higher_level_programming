#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """ text must be a string """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char in ".:?":
            print("\n\n")
