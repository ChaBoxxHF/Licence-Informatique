def Tri(M):
    lp=[]   #liste de compteurs pairs
    i=0     #itérateur de la boucle 1
    tmp=[]
    while i<len(M):
        j=0   #itérateur de la boucle 2
        cptp=0  #compteur de nombres pair
        while j<len(M[i]):
            if M[i][j]%2==0:   #si l'interieur de T2 est pair alors le compteur prends +1 sinon on avance dans le T2
                cptp+=1
            j+=1
        lp+=[cptp]  #on rentre le compteur de pair dans une liste histoire de pouvoir trier la liste M a partir de cette liste
        i+=1
        tmp+=[(cptp,i)]
    print(tmp)
    a=0
    while a<len(lp):
        k = lp[a]
        b = a
        while b>0 and lp[b-1]>k:                  #tri insetion
            lp[b]=lp[b-1]
            b-=1
        lp[b]=k
        a+=1
    return lp   #mon tableau est trié mais il faut redonner l'indice de lp a M
    #redonner M dans l'ordre

M = [[2,4,3,8],[0,0],[1,3,5,7]]
print(Tri(M))
