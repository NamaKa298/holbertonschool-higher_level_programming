#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        print("")
        return
    sortie = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            maj = ord(str[i]) - 32
        else:
            maj = ord(str[i])
        sortie += "{}" .format(chr(maj))
    print(sortie)
