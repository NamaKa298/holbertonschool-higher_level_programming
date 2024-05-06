#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        return
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            maj = ord(str[i]) - 32
        else:
            maj = ord(str[i])
        if i < len(str) - 1:
            print("{}" .format(chr(maj)), end='')
        else:
            print("{}" .format(chr(maj)))
