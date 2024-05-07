#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    else:
        somme = 0
        for i in range(1, len(sys.argv)):
            entier = int(sys.argv[i])
            somme += entier
    print("{}" .format(somme))
