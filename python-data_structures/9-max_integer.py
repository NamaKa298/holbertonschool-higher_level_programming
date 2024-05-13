#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        valeur_max = int()
        for i in my_list:
            if i > valeur_max:
                valeur_max = i
    return valeur_max
