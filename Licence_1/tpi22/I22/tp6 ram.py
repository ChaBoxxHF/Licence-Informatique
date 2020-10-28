from math import *
from random import *

def init_ram_list(height):
    liste = []
    i=0
    while i<height:
        liste+=[0]
        i+=1
    return liste

def fill_ram_random(ram,n):
    i=0
    l=ram
    while i<n:
        j=randrange(0,len(l))
        if l[j]==0:
            l[j]=randrange(1,256)
            i+=1
    return(l)

def fill_ram_place(ram,n):
    cpt=0
    while cpt<n:
        i=randrange(0,len(ram)-1)
        if ram[i]==0:
            ram[i]=i
            cpt+=1
    return(ram)
    
def get_value_list(ram,adresse):
    return(ram[adresse])
