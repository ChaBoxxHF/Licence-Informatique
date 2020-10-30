def parcours(n):
    i=0 #ligne
    l=[]
    cpt=0
    if n<=2:
        while i<n:
            j=0 #colonne
            while j<n:
                l+=[(i,j)]
                j+=1
            i+=1
    else:
        if cpt<(n**2)//2:
            while i<n:
                j=0
                while j<n:
                    l+=[(i,j)]
                    j+=1
                i+=1
                cpt+=1
        elif cpt>=(n**2)//2:
            while i<n:
                j=0
                l+=[(i,j+1)]
                #aucune idée de la façon de continuer l'algo de parcours
    return l

def rangement(T):
    chiant2ouf

def swap(M,a,b):
    temp=b
    b=a
    a=temp

def tri(M):
    i=0
    j=0
    h=0
    cpt=0
    l=[]
    while i<M:
        

def recherche(T,x):
    a=len(T)//3
    i=0
    cpt=0
    while i<len(T):
        if x==a:
            return cpt
        elif x<a:
            a=a//2
        elif x>a:
            a=(len(T)+a)//2
        cpt+=1
        i+=1
    return 0

def parcoursv2(n):
    i=0 #ligne
    l=[]
    cpt=0
    while i<(n**2)//2:
        l+=[(i,j)]
        i+=1
    while i<(n**2)-(n-1):
        l=l+[(i,j+1)]
