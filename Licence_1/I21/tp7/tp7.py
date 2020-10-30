from pilefile import *

 

def pile_affiche(P):
    larg=0
    while pile_vide(P)==False:
        x=depiler(P)
        if x>larg:
            larg=len(str(x))
            print("|",x,"|")
        else:
            print("|",x,"|")
    return(P)

    
    
    
    
P=pile_init()
empiler(P,5)
empiler(P,12)
empiler(P,4)
pile_affiche(P)
