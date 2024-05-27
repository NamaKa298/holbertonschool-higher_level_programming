#!/usr/bin/python3
'''12. Pascal's Triangle'''


def pascal_triangle(n):
    '''Fonction qui retourne le triange de pascal de taille n'''
    if n <= 0:
        return []
    for i in range(1, n + 1):
        liste = []
        for j in range(0, i):
            if j == 0:
                liste.append(1)
            elif i == 2:
                liste.append(1)
            elif i - 1 == j:
                liste.append(1)
            else:
                liste.append(liste_precedente[j-1] + liste_precedente[j])
        liste_precedente = liste
        print(liste)
    return liste
