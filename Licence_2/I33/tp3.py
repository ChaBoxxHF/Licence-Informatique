#exo 1

def decompose(n):
    l=[]
    while n!=0:
        l+=[n%2]
        n//=2
    return l[::-1]

#exo 2

def eval_poly(P,b):
    i=0
    pb=0
    while i<len(P)-1:
        pb+=P[i]
        pb*=b
        i+=1
    pb+=P[i]
    return pb

#exo 3

def multbyalpha(b,f):
    resultat = b << 1
    taille = len(bin(f)) - 3
    if ((resultat & (1 << taille)) != 0):
        resultat = resultat ^ f
    return resultat

#exo 4

def multiplie(x, y, P):
    pass

#exo 5

def multiplication(b, c, f):
    m=0
    aux=c
    while (b != 0):
        if (b & 1) != 0:
            max ^= aux
        aux = multbyalpha(aux, f)
        b >>= 1
    return m

#print(decompose(8245))
#print(eval_poly([3,5,4],1))
#print(multbyalpha(6,19))