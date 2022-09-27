#!/usr/bin/python3
"""
This module is designed to append text
to the EOF
"""


def append_write(filename="", text=""):
    """
    Function to append to 'filename' with passed of 'text'
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
