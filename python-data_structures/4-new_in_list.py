#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copie_liste = my_list.copy()
    if idx < 0:
        return copie_liste
    elif idx >= len(my_list):
        return copie_liste
    else:
        copie_liste[idx] = element
        return copie_liste
