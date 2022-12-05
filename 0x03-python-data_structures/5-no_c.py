#!/usr/bin/python3
def no_c(my_string):
    if "c" in my_string:
        idx = my_string.index("c")
        my_new_string = my_string[:idx] + my_string[idx+1:]
    if "C" in my_string:
        idx2 = my_string.index("C")
        my_new_string = my_string[:idx2] + my_string[idx2+1:]
    return my_new_string
