from pilefile import *

def eval_npi(exp) :
    P = pile_init()
    nb = ""
    for char in exp :
        if char.isdigit() :
            nb += char
        elif char != " " :
            a = depiler(P)
            b = depiler(P)
            r = int(eval(str(a)+char+str(b)))
            empiler(P, r)
        elif nb != "" :
            empiler(P, int(nb))
            nb = ""
    if nb != "" :
        empiler(P, int(nb))
    return depiler(P)
