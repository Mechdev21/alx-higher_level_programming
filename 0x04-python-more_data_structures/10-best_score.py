#!/usr/bin/python3

# a function that:
# returns a key with the biggest integer value.

def best_score(a_dictionary):
    high = []
    if a_dictionary is None:
        return None
    for i in a_dictionary.values():
        high.append(i)
    high.sort(reverse=True)
    for key, value in a_dictionary.items():
        if value == high[0]:
            return key
