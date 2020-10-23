def bbr(T):
    """ Retourne la liste des indices des cases à
    échanger pour obtenir un tableau à trois couleurs
    trié en bleu/blanc/rouge"""
    b=0 #bleu
    w=1 #blanc
    r=len(T)-1 #rouge
    while w<r:
        if T[w]=="white":
            w+=1
        elif T[w]=="red":
            tmp=T[w]
            T[w]=T[r]  #echange blanc rouge
            T[r]=tmp
            r-=1
        else:
            tmp=T[w]
            T[w]=T[b] #echange blanc bleu
            T[b]=tmp
            w+=1

