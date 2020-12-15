#!/usr/bin/python3
def element_at(my_list, idx):

    list_len = len(my_list)

    if idx < 0 or list_len <= idx:
        return None

    return my_list[idx]
