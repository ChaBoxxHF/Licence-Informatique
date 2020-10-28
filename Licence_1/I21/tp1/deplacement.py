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
    case_F=[]
    i=col+1
    j=lig+1
    while i<=7 and j<=7:
        case_F.append[(i,j)]
        i+=1
        j+=1
    i=col-1
    j=lig-1
    while i>=0 and j>=0:
        case_F.append[(i,j)]
        i-=1
        j-=1
        i=col+1
    j=lig+1
    while i<=7 and j<=7:
        case_F.append[(i,j)]
        i+=1
        j-=1
    i=col-1
    j=lig-1
    while i>=0 and j>=0:
        case_F.append[(i,j)]
        i-=1
        j+=1
    return [case_F]

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
    return []
        
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
    return []

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
   
   return []

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
    case_P=[]
    if lig == 6:
        case_P= case_P+[col,lig-2]
    if lig == 6:
        case_P= case_P+[col,lig-1]
    else:
        case_P= case_P+[col,lig-1]
    return [case_P]
  
