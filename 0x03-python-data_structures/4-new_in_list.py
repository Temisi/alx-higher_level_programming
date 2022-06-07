#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    t = my_list.copy()
    if idx < 0:
        return t
    elif idx > len(t) - 1:
        return t
    else:
        t[idx] = element
        return t
