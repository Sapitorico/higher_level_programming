#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """ text must be a string """
    if type(text) != str:
        raise TypeError("text must be a string")
    """ no space at the beginning  or at the end of each printed line """
    words = text.split()
    new_text = ""
    for word in words:
        new_text += word
        if word[-1] in ".:?":
            new_text += "\n\n"
        else:
            new_text += " "
    print(new_text.strip(), end="")
