#exo 1

def decompose(n):
    l=[]
    #partie puissance
    if (n%2==0):
        cpt=0
        while(n%2==0):
            n=n//2
            cpt+=1
        l+=[[2,cpt]]
    i=3
    #partie décomposé
    while n!=1:
        cpt=0
        if(n%i==0):
            while(n%i==0):
                n=n//i
                cpt+=1
            l+=[[i,cpt]]
        i+=2
    return l

#print(decompose(99999876400))

def multbyalpha(b,f):
    resultat = b << 1
    taille = len(bin(f)) - 3
    if ((resultat & (1 << taille)) != 0):
        resultat = resultat ^ f
    return resultat

def table_alpha(P):
    m = len(bin(P)) - 3
    card = (1 << m)
    l = [0]*(card-1)
    v = 1
    cpt = 0
    while cpt < card-1:
        l[cpt] = v
        v = multbyalpha(v,P)
        cpt = cpt+1
    return l


print(table_alpha(13))

def decompose2(n):
    l=[]    #initialisation de liste
    while n!=0:    #tant que n différent de 0 on continu a rajouter dans la liste n et on fait un décallage a droite de n
        l=[n&1]+l
        n=n>>1
    return l    #on retourne la liste

#print(decompose2(29))


def inverse(x,P):
    n = len(bin(P)) - 3
    i = log_table[x]
    return alpha_table[((1 << n) - 1) - i]

print(inverse(4,13))
