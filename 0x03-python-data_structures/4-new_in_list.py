i#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len1 = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > len1:
        return my_list
    else:
        len2 = 0
        while len2 <= len1:
            if len2 == idx:
                new_list = [element if idx == i else n for i, n in enumerate(my_list)]
                return new_list
            len2 += 1
