#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if my_list is not None:
        length = len(my_list) - 1
        i = 0
        if idx > length:
            return None
        while i <= length:
            if i == idx:
                return my_list[i]
            i += 1
