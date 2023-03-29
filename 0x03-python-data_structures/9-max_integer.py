#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_ = my_list[0]
    for b in my_list:
        if b > max_:
            max_ = b
    return max_
