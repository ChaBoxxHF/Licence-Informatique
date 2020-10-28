from random import *

def rand_table(n,a,b):
    i=0
    l=[]
    while i<n:
        l+=[randrange(a,b)]
        i+=1
    return(l)

def tri_insertion(T):
    i=1
    cpt=0
    n=0
    while i<len(T):
        if T[i]<T[i-1]:
            P=0
            while T[i-P]<T[i-P-1] and i-P-1>=0:
                tmp=T[i-P]
                T[i-P]=T[i-P-1]
                T[i-P-1]=tmp
                P+=1
                cpt+=1
        cpt+=1
        i+=1
    return(cpt)

def tri_selection(T):
    n=len(T)
    x=0
    cpt=0
    while x<len(T):
        jmax=T[0]
        j=0
        i=1
        while i<n:
            if jmax<T[i]:
                j=i
                jmax=T[i]
            cpt+=1
            i+=1
        tmp=T[n-1]
        T[n-1]=jmax
        T[j]=tmp
        x+=1
        n-=1
    return(cpt)
