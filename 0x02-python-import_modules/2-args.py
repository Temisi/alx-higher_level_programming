#!/usr/bin/python3
from sys import argv


def main():
    m = len(argv) - 1

    if m < 1:
        print("{} arguments.".format(m))
    elif m == 1:
        print("{} argument:".format(m))
        print("{}: ".format(m) + argv[1])
    elif m > 1:
        print("{} arguments:".format(m))
        for a in range(1, len(argv)):
            print("{}: {}".format(m, argv[a]))


if __name__ == "__main__":
    main()
