#!/usr/bin/python3
"""Algorithm to find peak element in an unsorted array"""


def find_peak(list_of_integers):

    list = list_of_integers

    if not list:
        return None

    middle = int((len(list) - 1) / 2)

    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]

    if list[middle] < list[middle + 1]:
        return find_peak(list[middle + 1:])
    else:
        return find_peak(list[:middle + 1])
