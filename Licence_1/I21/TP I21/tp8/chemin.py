from pilefile import *


def voisins(grille,lig,col):
    #retourne la liste des cases voisines vides de la cases (lig,col) de la grille <grille>
    L=[]
    l=lig
    c=col
    D=[(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in D:
        x=l+dx
        y=c+dy
        if 0<=x<len(grille) and 0<=y<len(grille[x]):
            if grille[x][y]!=1:
                L+=[(x,y)]
    return L

def chemin(grille, dep, arr):
    
    return [(depart)]

if __name__=='__main__':
    grille = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
              [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
              [2, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
              [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
              [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    print(set(voisins(grille,(3, 2))) == set([(3, 1), (2, 2)]))
    print(set(voisins(grille,(3, 5))) == set([(3, 4), (3, 6)]))
    print(set(voisins(grille,(6, 4))) == set([(6, 3)]))
    print(set(voisins(grille,(4, 21))) == set([(5, 21)]))
    print(set(voisins(grille,(6, 21))) == set([(5, 21)]))
    print(set(voisins(grille,(1, 14))) == set([(1, 13), (1, 15), (2, 14)]))
    print(set(voisins(grille,(4, 4))) == set([(4, 3), (3, 4)]))
    print(set(voisins(grille,(5, 19))) == set([(5, 20), (4, 19), (6, 19)]))
    print(set(voisins(grille,(7, 3))) == set([(6, 3)]))
    print(set(voisins(grille,(3, 21))) == set([(3, 20)]))

    print(len(chemin(grille, (3,0), (5,21))) == 31)    
    print(len(chemin(grille, (3,19), (4,4))) == 20)
        
