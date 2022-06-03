#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    mas = 0
    for b in argv[1:]:
        mas += int(b)
    print("{:d}".format(mas))
