#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        y = my_list[j]
        try:
            print("{:d}".format(y), end="")
             i += 1
        except Exception:
             pass
    print("")
    return i
