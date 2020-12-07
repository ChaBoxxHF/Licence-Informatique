import math
import copy
import time
from random import *



def genmatrix(n,p,t):
	M = []
	for i in range(n):
		aux = []
		for j in range(p):
			aux = aux + [random.randrange(t)]
		M = M + [aux]
	return M


def gendiag(n,t):
	M = [0]*n
	for i in range(n):
		M[i] = [0]*n
		M[i][i] = random.randrange(t)
	return M


def gentrianginf(n,t):
	M = []
	for i in range(n):
		aux = []
		for j in range(i):
			aux = aux + [random.randrange(t)]
		aux = aux + [random.randrange(1,t)]
		aux = aux + [0]*(n-i-1)
		M = M + [aux]
	return M


def gensym(n,t):
	M = gentrianginf(n,t)
	for i in range(len(M)):
		for j in range(i+1,len(M)):
			M[i][j] = M[j][i]
	return M


def genasym(n,t):
	M = gentrianginf(n,t)
	for i in range(len(M)):
		for j in range(i+1,len(M)):
			M[i][j] = -M[j][i]
	return M


def transpose(L):
	M = []
	for i in range(len(L[0])):
		aux = []
		for j in range(len(L)):
			aux = aux + [L[j][i]]
		M = M + [aux]
	return M


def gencirculante(L):
    M = [copy.copy(L)]
    n = len(L)
    for i in range(1,n):
        M = M + [[M[i-1][n-1]] + M[i-1][0:n-1]]
    return M


def gen_circulante2(n,t):
    M = [n]
    for i in range(1,t):
        b = M[i-1] & 1
        aux = (M[i-1] >> 1) ^ (b << (t-1))
        M = M + [aux]
    return M


def liste_perm(n):
	L = []
	for i in range(n):
		L = L + [i]
	cpt = 1
	while n >= 2:
		pos = random.randrange(n)
		L[pos], L[n-1] = L[n-1], L[pos]
		cpt = cpt + 1
		n = n - 1
	return(L)


def genmatrixperm(n):
	M = [0] * n
	position = liste_perm(n)
	for i in range(n):
		M[i] = [0]*n
		M[i][position[i]] = 1
	return M


def genmatrixperm2(n):
	M = [0] * n
	position = liste_perm(n)
	for i in range(n):
		M[i] = 1 << position[i]
	return M


def vect(L):
    T =[]
    k = len(L)
    n = len(L[0])
    # pour parcourir toutes les combinaisons lineaires a
    # k coefficients sur F_2, il suffit de parcourir 
    # les entiers de 0 a 2^k-1 et de regarder leur
    # decomposition en base 2
    i = 0
    while i < (1 << k):
        j = 0
        aux = [0]*n
        while j < k:
            # si en base 2, l'entier i comporte un
            # 1 en position j, alors il faut ajouter dans
            # la combinaison lineaire courante le jème vecteur
            # de la famille
            if ((1 << j) & i):
                cpt = 0
                while cpt < n:
                    aux[cpt] ^= L[j][cpt]
                    cpt = cpt + 1
            j = j + 1
        i = i + 1
        # si le vecteur n'a pas deja ete obtenu (la famille est peut etre liee)
        # on le rajoute au resultat final
        if  aux not in T:
            T = T + [aux]
    return T


































