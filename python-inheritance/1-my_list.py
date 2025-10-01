#!/usr/bin/python3
"""Define a class MyList that inherits from list:"""

class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        list_ = self[:]
        list_.sort()
        print(list_)
