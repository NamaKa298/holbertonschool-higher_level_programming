#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string.isalnum() or roman_string == None:
        return 0
    dictionnaire_chiffre_romain={'I' : 1, 'X' : 10, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    valeur = 0
    l =0
    for i in range(0, len(roman_string)-1):
        if dictionnaire_chiffre_romain[roman_string[i]] >= dictionnaire_chiffre_romain[roman_string[i+1]]:
            valeur += dictionnaire_chiffre_romain[roman_string[i]]
        else:
            valeur -= dictionnaire_chiffre_romain[roman_string[i]]
        l += 1
    if dictionnaire_chiffre_romain[roman_string[l]] > dictionnaire_chiffre_romain[roman_string[l-1]]:
        valeur += dictionnaire_chiffre_romain[roman_string[l]]
    else:
        valeur += dictionnaire_chiffre_romain[roman_string[l]]
    return(valeur)
