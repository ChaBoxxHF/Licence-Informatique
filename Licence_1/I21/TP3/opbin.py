from math import log, floor

def bit(n,i):
    """Retourne 1 si le <i>eme bit de <n> est a 1 et 0 sinon"""
    return

def set_bit(x, i, val):
    """Retourne la valeur de l'entier <x> 
    dont le <i>eme bit a pris la valeur <val>"""
    return

def pop_count(x):
    """Retourne le nombre de bits à 1 de l'entier <n>"""
    return

if __name__=='__main__':
    print("Test de bit()")
    print(bit(12, 0), 0, bit(12, 0)==0)
    print(bit(12, 1), 0, bit(12, 1)==0)
    print(bit(12, 2), 1, bit(12, 2)==1)
    print(bit(12, 3), 1, bit(12, 3)==1)
    print("\nTest de set_bit()")
    print(set_bit(12, 0, 1), 13, set_bit(12, 0,1)==13)
    print(set_bit(12, 2, 0), 8, set_bit(12, 2, 0)==8)
    print(set_bit(12, 5, 1), 44, set_bit(12, 5,1)==44)
    print(set_bit(12, 3, 0), 4, set_bit(12, 3,0)==4)
    print("\nTest de pop_count()")
    print(pop_count(9), 2, pop_count(9)==2)
    print(pop_count(16), 1, pop_count(16)==1)
    print(pop_count(27), 4, pop_count(27)==4)
    print(pop_count(31), 5, pop_count(31)==5)
