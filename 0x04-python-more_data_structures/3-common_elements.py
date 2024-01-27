#!/usr/bin/python3

# a function common elements that:
# returns a set of common elements in two sets

def common_elements(set_1, set_2):
    common = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common.append(i)
    return common
