from random import *
from math import *

def somme_pair(L):
    i=0
    s=0
    for i in range(len(L)):
        if L[i]%2==0:
            s+=L[i]
    return s

def somme_ind_pair(L):
    i=0
    s=0
    while i<len(L):
        s+=L[i]
        i+=2
    return s

def minimum(L):
    i=1
    min=L[0]
    while i<len(L):
        if min>L[i]:
            min=L[i]
        i+=1
    return min

def minimum2(L):
    i=0
    min1=L[0]
    min2=L[1]
    if min1<min2:
        tmp=min1
        min1=min2
        min2=tmp
    while i<len(L):
        if min1>L[i]:
            tmp=min1
            min1=L[i]
            min2=tmp
        elif min2>L[i] and min1<L[i]:
            min2=L[i]
        i+=1
    return min2

def minimum_pos(L):
    i=0
    l=[]
    min1=L[0]
    while i<len(L):
        if min1>L[i]:
            min1=L[i]
            l=[i]
        elif min1==L[i]:
            l+=[i]
        i+=1
    return l
    

def som_div_propres(n):
    if n<=1:
        return 0
    i=2
    s=1
    while i<sqrt(n):
        if n%i==0:
            s+=i
            s+=n//i
        i+=1
    if sqrt(n)==0:
        s+=sqrt(n)
    return s


def amicaux(n):
	l = []
	i = 2
	while i <= 2**n:
		j = som_div_propres(i)
		if j > i and som_div_propres(j) == i:
			l+=[(i, j)]
		i += 1
	return l

def tri(L):
    i=0
    while i<len(L):
        min1=L[i]
        mini=i
        j=i
        while j<len(L):
            if L[j]<min1:
                min1=L[j]
                mini=j
            j+=1
        tmp=L[i]
        L[i]=min1
        L[mini]=tmp
        i+=1
    return L

def tri_bulle(L):
    i=0
    while i<len(L):
        l=0
        r=1
        while r<len(L)-i:
            if L[r]<L[l]:
                tmp=L[l]
                L[l]=L[r]
                L[r]=tmp
            l+=1
            r+=1
        i+=1
    return L  

def partition(L):
    i=0
    while i<len(l):
        checkvalues=L[i]
        pass

def majoritaire(L):
    i=0
    n=len(L)
    b2ol=True
    while i<n and b2ol==True:
        cpt=0
        for j in L:
            if j==L[i]:
                cpt+=1
        b2ol= cpt<=n/2
        i+=1
    if b2ol==True:
        return False
    else:
        return L[i-1]

def recherche(L,S,p):
    t=[]
    i=0
    while i<len(L)-p:
        s=L[i]
        j=i+1
        while j<=p+i:
            s+=L[i]
            j+=1
        if s>=S:
            t+=[i]
        i+=1
    return t

#print(somme_pair([3,2,5,7,4,1]))
#print(somme_ind_pair([3,2,5,7,4,1]))
#print(somme_ind_pair([9, 7, 9, 2, 10, 7, 0, 11]))
#print(somme_ind_pair([7, 11, 6, 5, 7, 4, 9, 4, 12, 4, 10]))
#print(minimum([3,2,5,7,2]))
# print(minimum2([8, -16, 18, 14, -5, -14]))
# print(minimum2([-4, -15, -18, 4, -19, -13, 5]))
# print(minimum2([13, -18, 9, 7, -18]))
#print(minimum_pos([-20, -8, 3, -20, 3, -20, 17, -5, 14, -20, -20]))
#print(som_div_propres(randint(3,50)))
#print(amicaux(11))
#print(tri([8, -1, 2, 5, 3, -2]))
#print(tri_bulle([8, -1, 2, 5, 3, -2]))