#!/usr/bin/python3

# safe_print_integer: a function that:
# prints an integer

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except TypeError:
        print("This is a typr error")
