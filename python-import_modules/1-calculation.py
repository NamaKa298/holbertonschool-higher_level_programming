#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    resultat_add = add(a, b)
    print("{} + {} = {}".format(a, b, resultat_add))
    resultat_sub = sub(a, b)
    print("{} - {} = {}".format(a, b, resultat_sub))
    resultat_mul = mul(a, b)
    print("{} * {} = {}".format(a, b, resultat_mul))
    resultat_div = div(a, b)
    print("{} / {} = {}".format(a, b, resultat_div))
