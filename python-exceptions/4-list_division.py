#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nouvelle_liste =[]
    try:
        for i in range(list_length):
            try:
                resultat = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                resultat = 0
                print("division by 0")
            except TypeError:
                resultat = 0
                print("wrong type")
            except IndexError:
                resultat = 0
                print("out of range")
            nouvelle_liste.append(resultat)
    finally:
        return nouvelle_liste
