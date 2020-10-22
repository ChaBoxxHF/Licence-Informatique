#
# FIchier à compléter: parcours.py
#
# Chaque fonction retourne la liste des paires d'indices correspondant
# au parcours nommé.
#

def parcours_ligne(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours tableau de taille n x n en ligne.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,4,5,6,7,8,9 et la 
    fonction retournera la liste d'indices [(0,0),(1,0),(2,0),(0,1) ...]

    """
    print("parcours ligne:")
    i=0 #ligne
    l=[]
    while i<=n-1:
        j=0 #colonne
        while j<=n-1:
            l+=[(j,i)]
            j+=1
        i+=1
    return l

    
def parcours_colonne(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en colonne.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,4,7,2,5,8,3,6,9 et la 
    fonction retournera la liste d'indices [(0,0),(0,1),(0,2),(1,0) ...]

    """
    print("parcours colonne")
    j=0 #colonne
    l=[]
    for j in range(n):
        i=0 #ligne
        for i in range(n):
            l+=[(j,i)]
            i+=1
        j+=1
    return l
    
def parcours_diagonal(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en diagonale.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 3,2,6,1,5,9,4,8,7 et la 
    fonction retournera la liste d'indices [(2,0),(1,0),(2,1),(0,0) ...]

    """
    print("parcours diag")
    col=n-1
    lig=0
    l=[]
    #on effectue la partie suppérieure de la diagonale
    while col>=0:
        i=lig
        j=col
        while i<n and j<n:
            l+=[(j,i)]
            i+=1
            j+=1
        col-=1
    lig=1
    col=0
    #on effectue la partie inférieure de la diagonale
    while lig<n:
        i=lig
        j=col
        while i<n and j<n:
            l+=[(j,i)]
            i+=1
            j+=1
        lig+=1
    return l 
    
def parcours_antidiagonal(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en anti-diagonale.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 9,6,8,3,5,7,2,4,1 et la 
    fonction retournera la liste d'indices [(2,2),(2,1),(1,2),(2,0) ...]

    """
    print("parcours antidiag")
    col=n-1
    lig=n-1
    l=[]
    #on effectue la partie inférieur de l'antidiagonale
    while col>0:
        i=lig
        j=col
        while i>0 and j<n:
            l+=[(i,j)]
            i-=1
            j+=1
        col-=1
    lig=0
    col=n-1
    #on effectue la partie supérieur de l'antidiagonale
    while col>=0:
        i=lig
        j=col
        while i<n and j>=0:
            l+=[(j,i)]
            i+=1
            j-=1
        col-=1
    return l
   
def bhserp(n,j,l):
    i=n-1
    for i in range(n-1,-1,-1):
        l+=[(j,i)]
    return l

def hbserp(n,j,l):
    i=0
    for i in range(0,n):
        l+=[(j,i)]
    return l

def gdserp(n,i,l):
    j=0
    for j in range(0,n):
        l+=[(j,i)]
    return l

def dgserp(n,i,l):
    j=n-1
    for j in range(n-1,-1,-1):
        l+=[(j,i)]
    return l

def parcours_serpentin(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en serpentin.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,6,9,8,7,4,5 et la 
    fonction retournera la liste d'indices [(0,0),(1,0),(2,0),(2,1) ...]

    """
    i=0
    j=0
    l=[]
    if n//2==0:
        while j<=n//2+1:
            if i==0:
                hbserp(n,j,l)
            elif i==n:
                j=n
                bhserp(n,j,l)
    elif n//2==1:
        pass
    return l

print(parcours_serpentin(2))

def parcours_hb(n,j,l):
    ###effectuer un parcours de la ligne du haut vers le bas###
    i=0
    for i in range(0,n):
        l+=[(j,i)]
    return l

def parcours_bh(n,j,l):
    ###effectuer un parcours de la ligne du bas vers le haut###
    i=n-1
    for i in range(n-1,-1,-1):
        l+=[(j,i)]
    return l

def parcours_sinusoidal(n): 
    """Retourne la liste des indices (ligne,
    colonne) des cases correspondant a un parcours sinusoidal d'un
    tableau de taille n x n.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,4,7,8,5,2,3,6,9 et la 
    fonction retournera la liste d'indices :
    [(0,0),(1,0),(2,0),(2,1),(2,2) ...]

    """
    print("parcours_sinusoidal")
    j=0
    l=[]
    while j<n:
        if j%2==1: #si la ligne est paire alors on effectue le parcours partant de la droite sinon on effectue l'autre
            parcours_bh(n,j,l)
        else:
            parcours_hb(n,j,l)
        j+=1
    return l

def parcours_gd(n,i,l):
    ###effectuer un parcours de la ligne de la gauche vers la droite###
    j=0
    for j in range(0,n):
        l+=[(j,i)]
    return l

def parcours_dg(n,i,l):
    ###effectuer un parcours de la ligne de la droite vers la gauche###
    j=n
    for j in range(n-1,-1,-1):
        l+=[(j,i)]
    return l

def parcours_zigzag(n):
    """Retourne la liste des indices (ligne,
    colonne) des cases correspondant a un parcours sinusoidal d'un
    tableau de taille n x n.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,6,5,4,7,8,9 et la 
    fonction retournera la liste d'indices :
    [(0,0),(0,1),(0,2),(1,2),(1,1) ...]

    """
    print("parcours_zigzag")
    i=0
    l=[]
    while i<n:
        if i%2==1: #si la ligne est paire alors on effectue le parcours partant de la droite sinon on effectue l'autre
            parcours_dg(n,i,l)
        else:
            parcours_gd(n,i,l)
        i+=1
    return l


#print(parcours_ligne(10))
#print(parcours_colonne(10))
#print(parcours_diagonal(10))
#print(parcours_antidiagonal(4))
#print(parcours_zigzag(5))
#print(parcours_sinusoidal(10))
#print(parcours_serpentin(10))