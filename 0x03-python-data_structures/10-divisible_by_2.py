#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my = []
    for f in my_list:
        my.append(True if f % 2 == 0 else False)
    return my
