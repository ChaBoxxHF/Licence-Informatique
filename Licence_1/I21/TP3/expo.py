from math import log, floor

def bit(n,i):
   return

def expo_gd(x,k):
    """Retourne la liste des valeurs intermediares 
    du calcul de x^k avec l'algorithme d'exponentiation 
    rapide de gauche a droite"""
    return 
    

def expo_dg(x,k):
    """Retourne la liste des valeurs intermediares 
    du calcul de x^k avec l'algorithme d'exponentiation 
    rapide de gauche a droite"""
    
    return 

if __name__=='__main__':
    print("Test de expo_gd()")
    tests = [(2,4,[1,2,4,16]),
             (3,3,[1,3,9,27]),
             (2,7,[1,2,4,8,64,128]),
             (2,0,[1])]
    for test in tests:
        res=expo_gd(*test[:-1])
        print(res, test[-1], res==test[-1])

    print("\nTest de expo_dg()")
    tests = [(2,4,[1,2,4,16,16]),
             (2,13,[1,2,2,4,16,32,256,32*256]),
             (3,5,[1,3,3,9,81,243]),
             (2,0,[1])]
    for test in tests:
        res=expo_dg(*test[:-1])
        print(res, test[-1], res==test[-1])
