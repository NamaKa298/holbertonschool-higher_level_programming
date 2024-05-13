#!/usr/bin/python3
def no_c(my_string):
    nouvelle_chaine = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            nouvelle_chaine += i
    return nouvelle_chaine
