#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    li = list_of_integers
    lg = len(li)
    if lg == 0:
        return
    md = lg // 2
    if (md == lg - 1 or li[md] >= li[md + 1]) and\
       (md == 0 or li[md] >= li[md - 1]):
        return li[md]
    if md != lg - 1 and li[md + 1] > li[md]:
        return find_peak(li[md + 1:])
    return find_peak(li[:md])
