#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        copie_de_str = str[:n] + str[n + 1:]
        return copie_de_str
    return str
