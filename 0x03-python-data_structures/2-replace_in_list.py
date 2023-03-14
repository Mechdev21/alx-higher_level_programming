#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len1 = len(my_list)
    if (idx < 0):
        return my_list
    elif (idx > len1):
        return my_list
    else:
        for i in range(len1 + 1):
            if (i == idx):
                my_list[i] = element
                return my_list
