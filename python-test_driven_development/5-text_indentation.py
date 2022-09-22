#!/usr/bin/python3
"""
This module is designed to use 1 function
text_indentation
"""


def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters
    Raises TypeError if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text[:]

    for delim in ".?:":
        list_text = string.split(delim)
        string = ""
        for i in list_text:
            i = i.strip(" ")
            string = i + delim if string is "" else string + "\n\n" + i + delim

    print(string[:-3], end="")
