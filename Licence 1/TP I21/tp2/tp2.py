from math import cos,sin,pi
import matplotlib.pyplot as plt
from random import randrange
from time import time

def intervalle(a,b,inc):
    l=[]
    i=a
    #d=inc
    #cpt=0
    #while d<=1:
    #    d*=10
    #    cpt+=1
    while i<=b:
        l+=[i]
        i+=inc
    return l


def valeurs_sin(l):
    lsin=[]
    for j in range(len(l)):
        s=sin(l[j])
        lsin+=[s]
    return lsin

def valeurs_cos(l):
    lcos=[]
    for j in range(len(l)):
        c=cos(l[j])
        lcos+=[c]
    return lcos


## On cree la liste des abscisses des point que l ’ on veut tracer
#abscisse = intervalle(-2*pi,2*pi,0.2)
##On cree la liste des ordonnees des points que l ’ on veut tracer :
#sinu=valeurs_sin(abscisse)
#cosi=valeurs_cos(abscisse)
## plot () trace les courbes correspondantes et show () les affiche
## a l ’ ecran .
#plt.plot( abscisse , cosi , abscisse ,sinu )
#plt.show()


#def multiplication(n1,n2):
#    multi=str(n1*n2)
#    l=[]
#    for i in range(len(multi)-1,-1,-1):
#        l+=[int(multi[i])]
#    l+=[0]
#    return l


#def multiplication(n1,n2):
#    n=(len(n1)+len(n2))
#    N3=[0 for i in range(0,n)]
#    for j in range(0,len(n2)):
#        r=0
#        for i in range(0,len(n1)):
#            p=N3[i+j]+(n1[i]*n2[j])+r
#            N3[i+j]=p%10
#            r=p//10
#        N3[i+j]=r
#        print(N3)
#    return N3

def multiplication(n1,n2):
    n=(len(n1)+len(n2))
    N3=[0 for i in range(0,n)]
    j=0
    while j<len(n2):
        r=0
        i=0
        while i<len(n1):
            p=N3[i+j]+(n1[i]*n2[j])+r
            N3[i+j]=p%10
            r=p//10
            i+=1
        N3[i+j]=r
        j+=1
    return N3

def time_mult_py(n,k):
    lim=10**n
    test=[]
    for i in range(k):
        n1=randrange(lim)
        n2=randrange(lim)
        test+=[(n1,n2)]
    start=time()
    for n1,n2 in test:
        n3=n1*n2
    end=time()
    timer=end-start
    return timer


def nombre_alea(n):
    cha="1"
    for i in range(n):
        cha+="0"
    a=str(randrange(0,int(cha)))
    l=[]
    for j in range(len(a)-1,-1,-1):
        l+=[int(a[j])]
    if len(l)<n:
        l+=[0]
    print(a)
    return l


def time_my_mult(n,k):
    lim=n
    test=[]
    for i in range(k):
        n1=nombre_alea(lim)
        n2=nombre_alea(lim)
        test+=[(n1,n2)]
    start=time()
    for n1,n2 in test:
        n3=multiplication(n1,n2)
    end=time()
    timer=end-start
    return timer

def time_plus(n,k):
    l=[]
    for i in range(k):
        l+=[randrange(0,n)]
    li=[]
    start=time()
    for j in range(len(l)):
        li= li+[l[j]]
    end=time()
    timer=end-start
    return timer

def time_inc(n,k):
    l=[]
    for i in range(k):
        l+=[randrange(0,n)]
    li=[]
    start=time()
    for j in range(len(l)):
        li+=[l[j]]
    end=time()
    timer=end-start
    return timer

def time_append(n,k):
    l=[]
    for i in range(k):
        l+=[randrange(0,n)]
    li=[]
    start=time()
    for j in range(len(l)):
        li.append([l[j]])
    end=time()
    timer=end-start
    return timer

def list_alea(n,k):
    l=[0]*n
    for i in range(len(l)):
        l[i]=randrange(0,k-1)
    return l

def time_min(n,k):
    start=time()
    for i in list_alea(n,k):
        a=min(list_alea(n,k))
    end=time()
    timer=end-start
    print(a)
    return timer

def time_max(n,k):
    start=time()
    for i in list_alea(n,k):
        b=max(list_alea(n,k))
    end=time()
    timer=end-start
    print(b)
    return timer

print(time_min(10,99))
print(time_max(10,99))