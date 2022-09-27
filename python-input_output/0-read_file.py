#!/usr/bin/python3
"""
This module is designed to read a file
and print the contents to stdout
"""


def read_file(filename=""):
    """ function to read a file """
    with open(filename) as f:
        for line in f:
            print(line, end="")
