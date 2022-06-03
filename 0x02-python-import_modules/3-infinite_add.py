#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    mas = 0
    for b in range(1, len(argv)):
        mas += int(argv[b])
    print("{:d}".format(mas))
