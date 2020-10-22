from random import *

def rand_table(n,a,b):
    i=0
    tab=[]
    while i!=n:
        tab+=[randrange(a,b+1)]
        i+=1
    return tab
    
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
    
# def recherche_binaire(T,x):
#     g=0
#     d=len(T)-1
#     m=g+d//2
#     i=0
#     cpt=0
#     while g<=d:
#         if x==T[m]:
#             return m, cpt
#         elif x<T[m]:
#             d=m-1
#             m=(g+d)//2
#             cpt+=2
#         elif x>T[m]:
#             g=m+1
#             m=(g+d//2)
#             cpt+=2
#     return -1,cpt
    
def recherche_binaire(T,x):
    a = 0
    b = len(T)-1
    m = (a+b)//2
    i = 0
    while a <= b :
        if T[m] == x :
            i += 1
            return m, i
        elif T[m] > x :
            i += 2
            b = m-1
        else :
            i += 2
            a = m+1
        m = (a+b)//2
    return -1, i
            
T=[0,1,5,8,14,15,19,22]
print(T)
print(recherche_binaire(T,8))