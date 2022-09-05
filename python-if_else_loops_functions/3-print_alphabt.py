#!/usr/bin/python3

for n in range(ord('a'), ord('z')+1):
    if n == ord('e') or n == ord('q'):
        continue
    print("{:c}".format(n), end="")
