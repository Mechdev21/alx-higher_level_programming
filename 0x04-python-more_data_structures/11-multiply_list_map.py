#!/usr/bin/python3

# a function that:
# returns a list with all values multiplied by a
# number without using any loops

def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        my_list = []
    new_list = list(map((lambda x: x*number), my_list))
    return new_list
