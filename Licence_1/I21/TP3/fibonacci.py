from math import log, floor


def fibo(n):
    """Retourne <n>ieme terme de la suite de Fibonacci"""
    return
    
def matmult(m1, m2):
    """Retourne le produit des matrice 2x2 <m1> et <m2>"""
    return

def matcarre(m):
    """Retourne le carre de la matrice 2x2 <m>"""
    return 

def fibo2(n):
    """Retourne le <n>ieme terme de la suite de Fibonacci"""
    return

if __name__=='__main__':
    print("Test de fibo()")
    tests = [(0,0), (1,1), (2,1), (3,2),
             (4,3), (5,5), (6,8), (7,13)]

    for test in tests:
        res=fibo(test[0])
        print(res, test[1], res==test[1])

    print("\nTest de matmult()")
    tests = [([[1, 1],[1, 0]],
              [[1, 1],[1, 0]],
              [[2, 1],[1, 1]]),
             ([[2, 1],[1, 1]],
              [[1, 1],[1, 0]],
              [[3, 2],[2, 1]]),
             ([[3, 2],[2, 1]],
              [[8, 5],[5, 3]],
              [[34, 21],[21, 13]])]
    
    for test in tests:
        res=matmult(*test[:-1])
        print(res, test[-1], res==test[-1])

    print("\nTest de fibo2()")
    
    for test in range(10):
        res=fibo2(test)
        print(res, fibo(test), res==fibo(test))
