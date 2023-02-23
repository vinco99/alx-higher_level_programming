#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            ex = my_list[i]

        except IndexError:
            break
        print("{}".format(ex), end="")
        i += 1
    print("")
    return i
