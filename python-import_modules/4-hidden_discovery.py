#!/usr/bin/python3
if __name__ == "__main__":
    with open hidden_4 as fichier:
    for noms in fichier:
        if noms[0] != '_':
            print("{}" .format(noms))