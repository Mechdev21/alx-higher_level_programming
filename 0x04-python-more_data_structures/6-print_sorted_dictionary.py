#!/usr/bin/python3

# a function that:
# prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    ord = []
    for i in a_dictionary.keys():
        ord.append(i)
    ord.sort()
    for i in ord:
        x = a_dictionary.get(i)
        print("{}: {}".format(i, x))
