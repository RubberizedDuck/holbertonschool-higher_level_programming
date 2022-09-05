#!/usr/bin/python3

for x in range(0, 9):
    for y in range(1, 10):
        if x < y and x < 8:
            print("{}{}, ".format(x, y), end="")
        elif x < y:
            print("{}{}".format(x, y), sep="")
