#!/usr/bin/python3

# safe_print_list: a function that:
# prints x element of a list

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        while(x > 0 and n < len(my_list)):
            print("{}".format(my_list[n]), end="")
            n += 1
            x -= 1
    except IndexError:
        print("This index is out of range")
    print()
    return n
