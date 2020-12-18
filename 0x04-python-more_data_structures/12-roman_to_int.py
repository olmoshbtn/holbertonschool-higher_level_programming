#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = dict_roman[roman_string[len(roman_string) - 1]]

    for i in range(len(roman_string) - 1):
        actual = dict_roman[roman_string[i]]
        after = dict_roman[roman_string[i + 1]]
        if actual < after:
            result -= actual
        else:
            result += actual
    return result
