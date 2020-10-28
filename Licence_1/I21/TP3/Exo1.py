from math import *

def bit(n,i):
    b = 1<<i
    return int(n&b ==b)

def set_bit(x,i,val):
    if bit(x,i)==0 and val==1:
        return (x + (1<<i))
    elif bit(x,i)==1 and val==0:
        return (x - (1<<i))

## fonction set bit Quentin L.
##def set_bit(x,i,val):
##    if val == 1:
##        b=val<<i
##        return x|b
##    if val == 0:
##        val=~val+2
##        b=val<<i
##        b=~b
##        return x&b

def pop_count(x):
    i=0
    cpt=0
    while i<=log(x,2):
        if (bit(x,i))==1:
            cpt+=1
        i+=1
    return cpt


def expo_gd(x,k):
    y=1
    L=[]
    l = floor(log(k)/log(x))+1
    for i in range (l-1,-1,-1):
        y=y*y
        L+=[y]
        if bit(k,i)==1:
            y=y*x
            L+=[y]
    return L
            
def expo_dg(x,k):
    L1=expo_gd(x,k)
    L2=[]
    i=len(L1)-1
    while i>=0:
        L2+=[L1[i]]
        i-=1
    return L2
