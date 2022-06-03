#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    m = len(sys.argv) - 1

    if m == 0:
        print("{} arguments.".format(i))
    elif m == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if m >= 1:
        m = 0
        for arg in sys.argv:
            if m != 0:
                print("{}: {}".format(m, arg))
                m += 1
