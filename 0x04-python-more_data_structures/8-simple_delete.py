#!/usr/bin/python3

# a function that:
# deletes a key in a dictionary

def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
        if i == key:
            del a_dictionary[key]
            break
    return a_dictionary
