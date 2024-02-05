#!/usr/bin/python3

# safe_print_list_integers: a function that:
# prints the first x element of a list

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    i = 0
    try:
        while x > 0:
            if type(my_list[n]) == int:
                print("{:d}".format(my_list[n]), end="")
                i += 1
            else:
                print("", end="")
            n += 1
            x -= 1
    except IndexError as ex:
        print()
        print("IndexError: {}".format(ex))
    print()
    return i
