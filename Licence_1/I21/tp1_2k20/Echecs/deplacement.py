#
# Fichier à compléter: deplacement.py
#
# Chaque fonction doit renvoyer la liste des indices (col,lig) des
# cases sur lesquelles la pièce en question peut aller.
#

def cases_fou(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: fou en (2,3) 
    - - - - - - - - - -
    |           x     |
    | x       x       |
    |   x   x         |
    |     F           |
    |   x   x         |
    | x       x       |
    |           x     |
    |             x   |
    - - - - - - - - - -

    """
    l=[]
    i=lig+1
    j=col+1
    while i<=7 and j<=7:
        l+=[(j,i)]
        i+=1
        j+=1
    i=lig+1
    j=col-1
    while i<=7 and j>=0:
        l+=[(j,i)]
        i+=1
        j-=1
    i=lig-1
    j=col-1
    while i>=0 and j>=0:
        l+=[(j,i)]
        i-=1
        j-=1
    i=lig-1
    j=col+1
    while i>=0 and j<=7:
        l+=[(j,i)]
        i-=1
        j+=1
    return l

def cases_tour(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer une tour positionnée sur la case (col, lig)

    Ex: tour en (5,3)
    - - - - - - - - - -
    |           x     |
    |           x     |
    |           x     |
    | x x x x x T x x |
    |           x     |
    |           x     |
    |           x     |
    |           x     |
    - - - - - - - - - -

    """
    i=lig+1
    j=col
    l=[]
    while i<=7:
        l+=[(j,i)]
        i+=1
    i=lig-1
    j=col
    while i>=0:
        l+=[(j,i)]
        i-=1
    i=lig
    j=col+1
    while j<=7:
        l+=[(j,i)]
        j+=1
    i=lig
    j=col-1
    while j>=0:
        l+=[(j,i)]
        j-=1
    return l

def cases_reine(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionnée sur la case (col, lig)

    Ex: dame en (6,1)
    - - - - - - - - - -
    |           x x x |
    | x x x x x x D x |
    |           x x x |
    |         x   x   |
    |       x     x   |
    |     x       x   |
    |   x         x   |
    | x           x   |
    - - - - - - - - - -

    """
    #codefou
    l=[]
    i=lig+1
    j=col+1
    while i<=7 and j<=7:
        l+=[(j,i)]
        i+=1
        j+=1
    i=lig+1
    j=col-1
    while i<=7 and j>=0:
        l+=[(j,i)]
        i+=1
        j-=1
    i=lig-1
    j=col-1
    while i>=0 and j>=0:
        l+=[(j,i)]
        i-=1
        j-=1
    i=lig-1
    j=col+1
    while i>=0 and j<=7:
        l+=[(j,i)]
        i-=1
        j+=1
    #codetour
    i=lig+1
    j=col
    while i<=7:
        l+=[(j,i)]
        i+=1
    i=lig-1
    j=col
    while i>=0:
        l+=[(j,i)]
        i-=1
    i=lig
    j=col+1
    while j<=7:
        l+=[(j,i)]
        j+=1
    i=lig
    j=col-1
    while j>=0:
        l+=[(j,i)]
        j-=1
    return l
    

def cases_roi(col,lig):
   """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un roi positionné sur la case (col, lig)

    Ex: Roi en (4,5)
    - - - - - - - - - -
    |                 |
    |                 |
    |                 |
    |                 |
    |      x x x      |
    |      x R x      |
    |      x x x      |
    |                 |
    - - - - - - - - - -

   """
   l=[]
   i=lig
   j=col
   
   return l

def cases_cavalier(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: cavalier en (3,3)
    - - - - - - - - - -
    |                 |
    |     x   x       |
    |   x       x     |
    |       C         |
    |   x       x     |
    |     x   x       |
    |                 |
    |                 |
    - - - - - - - - - -

    """
    return []

def cases_pion(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: pions en (1,6) et (5,3)
    - - - - - - - - - -
    |                 |
    |                 |
    |           x     |
    |           P     |
    |   x             |
    |   x             |
    |   P             |
    |                 |
    - - - - - - - - - -

    """
    i=lig+1
    j=col
    l=[]
    if lig==6:
        while i>=4:
            l+=[(j,i)]
            i+=1
    else:
        l+=[(j,i)]
    return l
  
