#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    m = len(argv) - 1
    print("{:d} argument{}".format(m, "s" if m != 1 else ""), end="")
    print("{}".format("." if m == 0 else ":"))
    if m > 0:
        for a in range(1, m + 1):
            print("{:d}: {}".format(a, argv[a]))
