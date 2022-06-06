#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for m in range(len(my_list)):
            print("{:d}".format(my_list[m]))
#    q = len(my_list) - 1
#    for m in my_list:
#        print("{:d}".format(my_list[q]))
#        q -= 1
# def print_reversed_list_integer(my_list=[]):
#    my_list.reverse()
#    for m in my_list:
#        print("{:d}".format(m))
# def print_reversed_list_integer(my_list=[]):
#   for n in reversed(my_list):
#      print("{:d}".format(n))
