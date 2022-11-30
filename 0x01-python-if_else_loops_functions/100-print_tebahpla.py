#!/usr/bin/python3
for i in range(0, 26, 2):
    print("{:c}".format(122-i), end="")
    print("{:c}".format(90-i-1), end="")
