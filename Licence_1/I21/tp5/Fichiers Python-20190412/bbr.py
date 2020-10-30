def bbr(T):
    """ Retourne la liste des indices des cases à
    échanger pour obtenir un tableau à trois couleurs
    trié en bleu/blanc/rouge"""
    i=0
    while i<T:
        j=0
        while j<T:
            if T[j]==blue:
                j+=1
            elif T[j]==white or red:
                tmp = T[j+1]
                T[j+1]=T[j]
                T[j]=tmp
                j+=1
        i+=1
