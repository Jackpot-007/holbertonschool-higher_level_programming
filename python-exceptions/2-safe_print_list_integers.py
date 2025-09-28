#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    for n in range(x):
        try:
            print(my_list[n], end="")
            numbers += 1
            print("{:d}".format(value))
        except IndexError:
            break
    print()
    return numbers
