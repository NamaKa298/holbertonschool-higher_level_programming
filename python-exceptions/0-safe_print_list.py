#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nombre_elements = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nombre_elements += 1
        except IndexError:
            pass
    print("")
    return nombre_elements
