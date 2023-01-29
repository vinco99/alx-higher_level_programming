#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    from l in range(x):
        try:
            print(my_list[l], end="")
            a += 1
        except IndexError:
            break
        print()
        return a
