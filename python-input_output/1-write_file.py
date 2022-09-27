#!/usr/bin/python3
"""
This module is designed to open a file
and write into it
"""


def write_file(filename="", text=""):
    """
    filename is the file to open
    and text is what we are writing to that file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
