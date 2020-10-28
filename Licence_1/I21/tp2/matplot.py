from math import *

def intervalle (a,b,inc):
    liste=[]
    i=a
    while a<=b:
        liste+=[a]
        a+=inc
    return liste

def valeur_sin(t):
    sinus=[]
    i=0
    while i<len(t):
        sinus+=[sin(t[i])]
        i+=1
    return sinus

def valeur_cos(t):
    cosinus=[]
    i=0
    while i<len(t):
        cosinus+=[cos(t[i])]
        i+=1
    return cosinus

import matplotlib.pyplot as plt
# On cree la liste des abscisses des point que l ’ on veut tracer
##abscisse = []
##for i in range(10):
##    abscisse += [ i ]

abscisse = intervalle(-2*pi,2*pi,0.1)
# On cree la liste des ordonnees des points que l ’ on veut tracer :
carre = []
for i in range( len ( abscisse )):
    carre += [ abscisse [ i ]**2]
cube = []
for i in range ( len ( abscisse )):
    cube += [ abscisse [ i ]**3]
# plot () trace les courbes correspondantes et show () les affiche
# a l ’ ecran .
plt.plot( abscisse , valeur_sin(abscisse) , abscisse , valeur_cos(abscisse) )
plt.show()



        
