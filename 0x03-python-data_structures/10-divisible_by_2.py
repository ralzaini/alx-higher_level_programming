#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list_divisibles = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            list_divisibles.append(True)
        else:
            list_divisibles.append(False)
    return list_divisibles
