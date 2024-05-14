#!/usr/bin/python3
def common_elements(set_1, set_2):
    nouvelle_liste = []
    for i in set_1:
        if i in set_2:
            nouvelle_liste.append(i)
    return nouvelle_liste
