#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    result = ""
    index = len(my_list) - 1
    while index >= 0:
        print("{}".format(result += my_list[index]))
        index -= 1
        return result
