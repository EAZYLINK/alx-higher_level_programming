#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for char in str:
        if str.index(char) == n:
            continue
        new_str += char
    return new_str
