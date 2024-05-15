#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_score = 0
    best_personne = ""
    for i in a_dictionary:
        if best_score < a_dictionary[i]:
            best_score = a_dictionary[i]
            best_personne = i
    return best_personne

