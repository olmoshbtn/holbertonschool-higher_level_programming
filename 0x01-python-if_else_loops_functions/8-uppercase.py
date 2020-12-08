#!/usr/bin/python3
def uppercase(str):
    print("{}".format(
        str.translate({(char | 32): char for char in range(ord('A'),
                                                           ord('Z') + 1)})))
