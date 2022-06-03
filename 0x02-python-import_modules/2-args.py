#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    print("{:d} argument{}".format(argc, "s" if argc != 1 else ""), end="")
    print("{}".format("." if argc == 0 else ":"))
    if argc > 0:
        for i in range(1, argc + 1):
            print("{:d}: {}".formar(i, argv[i]))
