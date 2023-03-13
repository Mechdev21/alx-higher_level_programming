#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    caount = len(my_list)
    if idx > caount:
        return None
    if my_list is not None:
        i = 0
        while i <= caount:
            if idx == i:
                return my_list[i]
            i += 1
