#!/usr/bin/python3
def best_score(a_dictionary):
    max = -999
    if a_dictionary == None:
        return None
    else:
        for value in a_dictionary.values():
            if value > max:
                max = value
    for key, value in a_dictionary.items():
        if value == max:
            return key
