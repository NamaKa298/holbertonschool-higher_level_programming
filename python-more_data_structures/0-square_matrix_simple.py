#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nouvelle_matrice = []
    for i in matrix:
        ligne_nouvelle_matrice = []
        for j in i:
            k = j**2
            ligne_nouvelle_matrice.append(k)
        nouvelle_matrice.append(ligne_nouvelle_matrice)
    return nouvelle_matrice
