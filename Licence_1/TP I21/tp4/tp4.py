from random import randrange
import matplotlib.pyplot as plt

def rand_table(n,a,b):
    l=[]
    for i in range(n):
        r=randrange(a,b+1)
        l+=[r]
    return l

#for i in range (5) : (print(rand_table(8, 4, 8)))

#def tri_bulle(tri):
#    l=[i for i in tri]
#    i=len(l)-1
#    cpt=0
#    while i > 0:
#        j=0
#        while j < i:
#            if l[j]>l[j+1]:
#                temp=l[j+1]
#                l[j+1]=l[j]
#                l[j]=temp
#            cpt+=1
#            j+=1
#        i-=1
#    return cpt



#def tri_insertion(tri):
#    l=[i for i in tri]
#    i=1
#    cpt=0
#    while i<len(l)-1:
#        j=i-1
#        k=l[i]
#        while j>=0 and k<l[j]:
#            l[j+1]=l[j]
#            j-=1
#            cpt+=1
#        l[j+1]=k
#        i+=1
#    return cpt

#def tri_selection(tri):
#    l=[i for i in tri]
#    cpt=0
#    for i in range(len(l)):
#        k=i
#        imin=i
#        while k<len(l):
#            if l[imin]>l[k]:
#                imin=k
#            k+=1
#        temp=l[imin]
#        l[imin]=l[i]
#        l[i]=temp
#        cpt+=1
#    return cpt

#def compare_tris(l):
    #t=(tri_selection(l),tri_insertion(l),tri_bulle(l),)
    #return t
#naninani

def retourner(T,i):
    return T[:i]+T[i:][::-1]

print(retourner([3, 2, 5, 2, 9, 7, 7, 3, 7, 2],6))

def tri_pancake(T):
    tri = [i for i in T]
    indexes = []

    for i in range(len(tri)):
        k, imax = i+1, i
        #recherche de la plus grande valeur de T
        while k < len(tri):
            if tri[imax] < tri[k]:
                imax = k
            k+=1
        #mettre la plus grande valeurs de T en haut
        if not imax == len(T) - 1:
            tri = retourner(tri, imax)
            indexes += [imax]
        #mettre la plus grande valeurs de T a sa place
        tri = retourner(tri, i)
        indexes += [i]

    return indexes

#l=rand_table(10,1,50)
#print(l)
#print (retourner(l,2))

def tri_bulle(T):
    exch = True
    i = 0
    cpt=0
    while exch == True:
        exch = False
        i = i + 1
        for j in range(0, len(T) - i):
            if T[j] > T[j+1]:
                exch = True
                temp=T[j+1]
                T[j+1]=T[j]
                T[j]=temp
            cpt+=1
    return cpt
##çamarche



#def tri_insertion(T):
#    cpt=0
#    for i in range(0,len(T)):
#        g = T[i]
#        j = i
#        while j>0 and T[j-1]>g:
#            T[j]=T[j-1]
#            j = j-1
#            cpt+=1
#        T[j]=g
#        cpt+=1
#    print (T)
#    return cpt

def tri_insertion(T):
    nb_comp=0
    for i in range(1,len(T)):
        j=i
        while j>0 and T[j]<T[j-1]:
            temp=T[j]
            T[j]=T[j-1]         #echanger#
            T[j-1]=temp
            nb_comp += 1
            j = j-1
        nb_comp += 1
    return nb_comp


def tri_selection(T):
    nb = len(T)
    cpt=0
    for i in range(0,nb):    
        min = i
        for j in range(i+1,nb) :
            if T[j] < T[min] :
                min = j
                cpt+=1
        if min is not i :
            temp = T[i]
            T[i] = T[min]
            T[min] = temp
            cpt+=1
        cpt+=1
    print(T)
    return cpt

print(tri_selection([2, 3, 3, 3]))


#def compare_tris(T):
#    return (
#        tri_insertion(T),
#        tri_bulle(T),
#        tri_selection(T)
#    )

#moyennes_c1 = [0] * 10
#moyennes_c2 = [0] * 10
#moyennes_c3 = [0] * 10
#for i in range(1,11):
#    j = i * 50
#    c1, c2, c3 = 0, 0, 0
#    for k in range(100):
#        T = rand_table(j, 1, j)
#        cc1, cc2, cc3 = compare_tris(T)
#        moyennes_c1[i - 1] = cc1
#        moyennes_c2[i - 1] = cc2
#        moyennes_c3[i - 1] = cc3
#    moyennes_c1[i - 1] /= 100
#    moyennes_c2[i - 1] /= 100
#    moyennes_c3[i - 1] /= 100

#print(i / 10 * 100, "%")

#I = [i * 50 for i in range(1, 11)]

#plt.subplot(221)
#plt.title("Insertion")
#plt.plot(I, moyennes_c1)
#plt.subplot(222)
#plt.title("Bulle")
#plt.plot(I, moyennes_c2)
#plt.subplot(223)
#plt.title("Selection")
#plt.plot(I, moyennes_c3)
#plt.show()