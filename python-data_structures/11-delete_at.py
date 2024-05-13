#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        nouvelle_liste = list()
        nouvelle_liste = my_list[:idx] + my_list[idx + 1:]
        my_list = my_list.remove(my_list[idx])
        return nouvelle_liste
