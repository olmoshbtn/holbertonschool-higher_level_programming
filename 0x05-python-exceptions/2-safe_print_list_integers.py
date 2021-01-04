#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (ValueError, TypeError):
            pass
        else:
            int_printed += 1
    print()
    return int_printed
