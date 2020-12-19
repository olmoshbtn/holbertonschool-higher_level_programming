#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key, value in list(a_dictionary.items()):
            if value == value:
                    del a_dictionary[key]
                    break
    return a_dictionary
