#!/usr/bin/python3
'''1. Divide a matrix'''


def matrix_divided(matrix, div):
    '''Function that divides all elements of a matrix'''
    nouvelle_matrice = []
    row_len_0 = len(matrix[0])
    for i in range(len(matrix)):
        ligne_nouvelle_matrice = []
        row_len = len(matrix[i])

        if row_len_0 != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if isinstance(matrix[i][j] / div, float):
                ligne_nouvelle_matrice.append(round(matrix[i][j] / div, 2))
            if isinstance(matrix[i][j] / div, int):
                ligne_nouvelle_matrice.append(round(matrix[i][j] / div, 0))
        nouvelle_matrice.append(ligne_nouvelle_matrice)
    return nouvelle_matrice
