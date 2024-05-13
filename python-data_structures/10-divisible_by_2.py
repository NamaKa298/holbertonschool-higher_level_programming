#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nouvelle_liste =list()
    for i in my_list:
        if i % 2:
            nouvelle_liste.append(True)
        else:
            nouvelle_liste.append(False)
    return nouvelle_liste
