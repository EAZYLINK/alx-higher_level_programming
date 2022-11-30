#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) <= 90:
            result += chr(ord(char))
        elif ord(char) >= 97:
            result += chr(ord(char)-32)
    print("{:s}".format(result))
