#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for w in m:
            print("{:d}".format(w), end="" if w is m[-1] else " ")
        print()
