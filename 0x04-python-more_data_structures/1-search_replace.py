#!/usr/bin/python3

# write a function search replace that
# replaces all occurrences of an element by another in a new list
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element

def search_replace(my_list, search, replace):
    n = len(my_list)
    i = 0
    while i < n:
        if my_list[i] == search:
            my_list[i] = replace
        i += 1
    return my_list
