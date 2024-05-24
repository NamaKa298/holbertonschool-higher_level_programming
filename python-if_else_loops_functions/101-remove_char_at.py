#!/usr/bin/python3
def remove_char_at(str, n):
    copie_de_str = str[:n] + str[n + 1:]
    return copie_de_str
