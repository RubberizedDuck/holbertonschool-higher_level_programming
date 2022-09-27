#!/usr/bin/python3


def read_file(filename=""):
    """ function to read a file """
    with open(filename) as f:
        for line in f:
            print(line, end="")
