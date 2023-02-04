#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """ text must be a string """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indent = False
    """no space at the beginning or at the end of each printed line"""
    for char in text:
        if char in ".?:":
            print(char, end="\n\n")
            indent = True
        elif indent and char == " ":
            continue
        else:
            indent = False
            print(char, end="")
