from random import *

def gen_cle_hill(n):
    mat=[]
    i=0
    vec=[]
    while i<n:
        mat+=[[0]*n]
        vec+=[0]
        i+=1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j]=randint(0,28)
            vec[j]=randint(0,28)
    mat+=[vec]
    return mat

print(gen_cle_hill(3))