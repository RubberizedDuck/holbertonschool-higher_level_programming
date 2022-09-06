#!/usr/bin/python3


def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            char = ord(char) - 32
        else:
            char = ord(char)
        print("{}".format(chr(char)), end="")
    print("")
