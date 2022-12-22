#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except:
            print("{} is bigger than number of elements".format(x))
            print()
