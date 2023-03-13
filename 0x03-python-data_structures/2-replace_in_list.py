#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len1 = len(my_list)
    len2 = 0
    if (idx < 0):
        return my_list
    if (idx > len1):
        return my_list
    if my_list is not None:
        for i in my_list:
            if (len2 == idx):
                my_list[len2] = element
                return my_list
            len2 += 1
