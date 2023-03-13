#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    if my_list is not None:
        a = 0
        for i in my_list:
            if a == idx:
                my_list[a] = element
                return my_list
            a += 1
