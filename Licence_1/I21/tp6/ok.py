from random import *

### tableau trié
def gen_tableau(n):
    i=0
    tab=[]
    while i<n:
        tab+=[randrange(2*n+1)]
        i+=1
    for k in range(1,len(tab)):
        temp=tab[k]
        j=k
        while j>0 and temp<tab[j-1]:
            tab[j]=tab[j-1]
            j-=1
            tab[j]=temp
    return tab

def recherche_binaire(T,x):
    g=0
    d=len(T)-1
    m=(g+d)//2
    ###cpt=0
    while g<=d:
        if x==T[m]:
            return m
            ###return cpt
        elif x<T[m]:
            d=m-1
            m=g+d//2
        elif x>T[m]:
            g=m+1
            m=(g+d)//2
        ###cpt+=1
    
    return -1

def recherche_terciaire(T,x):
    g=0
    d=len(T)-1
    m1=(g+d)//3
    m2=(2*(g+d)//3)
    cpt=0
    while g<=d:
        if x==T[m1]:
            return m1
            ###return cpt
        if x==T[m2]:
            return m2
            ###return cpt
        elif x<T[m1]:
            d=m1
            m1=g+d//2
        elif x>T[m1]:
            g=m1
            d=m2
            m1=(g+d)//2
        elif x<T[m2]:
            d=m2
            g=m1
            m2=g+d//2
        elif x>T[m2]:
            g=m2
            m2=(g+d)//2
        ###cpt+=1
    return -1



T=gen_tableau(10)
print(T)
print(recherche_terciaire(T,12))

