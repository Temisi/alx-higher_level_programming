#!/usr/bin/python3
def uppercase(str):
    for n in str:
        print("{}".format(chr(ord(n) - 32) if n >= "a"
                          and n <= "z" else n), end="")
    print()
