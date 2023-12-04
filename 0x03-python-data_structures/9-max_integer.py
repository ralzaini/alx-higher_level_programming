#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    my_copy = my_list.copy()
    my_copy.sort()
    return my_copy[-1]
