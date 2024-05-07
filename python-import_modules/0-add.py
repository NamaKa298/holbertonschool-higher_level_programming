#!/usr/bin/python3
if __name__ == "__main__":
    add = __import__('0-import_add').add
    a = 1
    b = 2
    resultat = add(a, b)
    print ("{} + {} = {}".format(a, b, resultat))