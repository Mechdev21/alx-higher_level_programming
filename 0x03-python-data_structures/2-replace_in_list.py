#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len1 = len(my_list) - 1
    len2 = 0
    if (idx < 0):
        return my_list
    elif (idx > len1):
        return my_list
    else:
        while len2 <= len1:
            if len2 == idx:
                my_list[idx] = element
                return my_list
            len2 += 1
