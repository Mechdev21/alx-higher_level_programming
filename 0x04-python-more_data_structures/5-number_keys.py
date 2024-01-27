#!/usr/bin/python3

# a function that:
# returns the number of keys in a dictionary

def number_keys(a_dictionary):
    count = 0
    lt = []
    for i in a_dictionary.keys():
        lt.append(i)
    count = len(lt)
    return count
