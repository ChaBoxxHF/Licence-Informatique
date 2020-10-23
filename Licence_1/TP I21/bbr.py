def bbr(T):
    """ Retourne la liste des indices des cases à
    échanger pour obtenir un tableau à trois couleurs
    trié en blue/white/red"""
    b=0
    w=0
    r=len(T)-1
    i1=0
    i2=0
    l=[]
    while w<r:
        if T[w]=="white":
            w+=1
        elif T[w]=="red":
            tmp=T[w]
            T[w]=T[r]
            T[r]=tmp
            i1=w
            i2=r
            r-=1
        else:
            tmp=T[w]
            T[w]=T[b]
            T[b]=tmp
            i1=w
            i2=b
            b+=1
            w+=1
        l+=[(i1,i2)]
    return l


print(bbr(['white','white','red','blue','blue','red','white']))