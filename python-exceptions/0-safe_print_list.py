#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nombre_elements = 0
    longueur = 0
    for elements in my_list:
        longueur += 1
    try:
        if x <= longueur:
            for i in range(x):      
                print(my_list[i], end = "")
                nombre_elements += 1
            print("")
        elif x > longueur:
            for i in range(longueur):      
                print(my_list[i], end = "")
                nombre_elements += 1
            print("")
    except:
        pass
    return nombre_elements
