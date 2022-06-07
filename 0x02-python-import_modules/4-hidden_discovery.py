#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for m in dir(hidden_4):
        if not m.startswith("__"):
            print(m)
