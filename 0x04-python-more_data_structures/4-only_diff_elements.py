#!/usr/bin/python3

#  function that
# returns a set of all elements present in only one set

def only_diff_elements(set_1, set_2):
    uniq = []
    for i in set_1:
        if i not in set_2:
            uniq.append(i)
    for j in set_2:
        if j not in set_1:
            uniq.append(j)
    return uniq
