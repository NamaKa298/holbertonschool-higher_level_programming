#!/usr/bin/env python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            maj = ord(str[i]) - 32
        else:
            maj = ord(str[i])
        if i < len(str) - 1:
            print(chr(maj), end='')
        else:
            print(chr(maj))