#!/usr/bin/python3
'''1. My list'''


class MyList(list):
    """
    Represent a custom list named my list
    """

    def print_sorted(self):
        '''class MyList that inherits from list'''
        print(sorted(self))
