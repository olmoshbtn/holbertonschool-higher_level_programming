#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    list_len = len(my_list)

    if idx < 0 or list_len <= idx:
        return my_list

    list_copy = my_list.copy()

    list_copy[idx] = element
    return list_copy
