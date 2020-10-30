from time import time
from random import randrange

def multiplication(n1,n2):
    n3=[0]*len(n1)*2
    n,j=len(n1),0
    while j<n:
        i=0
        r=0
        while i<n:
            p=n3[i+j]+n1[i]*n2[j]+r
            n3[i+j]=p%10
            r=p//10
            i+=1
        n3[i+j]=r
        j+=1
    return n3

def time_mult_py(n,k):
    lim=10**n
    test=[(randrange(lim),randrange(lim))for i in range(k)]
    start=time()
    for n1,n2 in test:
        n3=n1*n2
        end=time()
    return end-start
