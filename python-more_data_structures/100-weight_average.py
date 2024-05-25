#!/usr/bin/python3
def weight_average(my_list=[]):
    coeff_tot = 0
    valeur_mult_par_coeff = 0
    if my_list == []:
        return 0.00
    for tup in my_list:
        coeff_tot += tup[1]
        valeur_mult_par_coeff += tup[0] * tup[1]
    return valeur_mult_par_coeff/coeff_tot
