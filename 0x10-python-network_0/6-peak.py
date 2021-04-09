#!/usr/bin/python3
"""Algorithm to find peak element in an unsorted array"""


def find_peak(list_of_integers):

    list = list_of_integers
    length = len(list)

    if length == 0:
        return

    middle = length // 2

    if (middle == length - 1 or list[middle] >= list[middle + 1]) and\
       (middle == 0 or list[middle] >= list[middle - 1]):
        return list[middle]

    if middle != length - 1 and list[middle + 1] > list[middle]:
        return find_peak(list[middle + 1:])
    return find_peak(list[:middle])
