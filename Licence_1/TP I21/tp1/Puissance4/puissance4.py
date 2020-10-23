#############################################
# Jeu du Puissance 4                        #
# Cours d'algorithmique                     #
# Licence Informatique - 1ere année         #
# Université de Toulon                      #
#                                           #
# Version du 01/03/2019                     #
#############################################


def init_jeu():
    """Renvoie une grille de jeu 6x7 sous forme d'une
    liste de listes remplie de 0"""
    return [[0]*7 for i in range(6)]

def dessine_grille(grille):
    """Retourne sous forme de chaine de caracteres l'état de la grille de jeu 
    ainsi que le numéro des colonnes:
       -O pour le joueur 1
       -X pour le joueur 2
       
    """
    i=len(grille)-1
    gr=""
    while i>=0:
        j=0
        ligne=""
        while j<len(grille[i]):
            if grille[i][j]==0:
                ligne+=" "
            elif grille[i][j]==1:
                ligne+="O"
            elif grille[i][j]==2:
                ligne+="X"
            j+=1
        gr+= "|"+ ligne + "|\n"
        i-=1
    gr+="---------\n"
    gr+=" 0123456"
    return gr

def coups_legaux(grille):
    """Renvoie la liste des colonnes dans lesquelles il est possible de
    jouer un jeton

    """
    i=len(grille)-1
    l=[]
    while i>=0:
        j=0
        while j<len(grille[i]):
            if grille[i][j]==0 and j not in l:
                    l+=[j]
            j+=1
        i-=1
    return l

def jouer_coup(joueur, coup, grille):
    """Ajoute un jeton pour le joueur <joueur> dans la colonne <coup> dans
    la grille et renvoie la ligne où celui-ci a été joué

    """
    if joueur==1:
        print("c'est le tour du joueur 1")
        print(coups_legaux(grille))
        print("veuillez choisir un coup légal",coup)
        j=coup
        i=0
        while grille[i+1][j]==0:
            i+=1
        grille[i][j]="X"
    elif joueur==2:
        print("c'est le tour du joueur 2")
        print(coups_legaux(grille))
        print("veuillez choisir un coup légal",coup)
        j=coup
        i=0
        while grille[i+1][j]==0:
            i+=1
        grille[i][j]="X"
    return grille
    

def gagnant_colonne(lig, col, grille):
    """Renvoie True si le coup joué (lig,col) forme une colonne de 4 jetons
    False sinon
    """
    while lig<lig+4:
        if lig==lig+1:
            lig+=1
        else:
            return False
    return True

def gagnant_ligne(lig, col, grille):
    """Renvoie True si le coup joué (lig,col) forme une ligne de 4 jetons
    False sinon
    """
    return

def gagnant_diagonale(lig, col, grille):
    """Renvoie True si le coup joué (lig,col) forme une diagonale de 4 jetons
    False sinon
    """
    return

def gagnant_antidiagonale(lig, col, grille):
    """Renvoie True si le coup joué (lig,col) forme une antidiagonale de 4 jetons
    False sinon
    """
    return

def gagner(lig, col, grille):
    """Renvoie True si le coup joué est un coup gagnant
    False sinon
    """
    return

def main():
    """Programme principal:
    A chaque itération de la boucle de jeu il faut:
      - afficher l'état du jeu
      - calculer les coups légaux
      - stopper la partie si la liste est vide
      - demander un coup legal au joueur actif
      - ajouter son jeton dans la grille
      - arreter la partie si le coup est gagnant
      - changer le joueur actif et recommencer

    """
    pass
    
if __name__=='__main__':
    main()

#print (init_jeu())
print(dessine_grille([[0,2,1,2,1,1,0],
                    [0,1,2,2,1,0,0],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,2,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0]]))
#print(coups_legaux([[1,1,2,2,2,1,2],
                 #[2,2,1,1,1,2,1],
                 #[1,1,2,2,2,1,2],
                 #[2,2,1,1,0,2,1],
                 #[1,1,2,1,0,1,2],
                 #[0,2,2,1,0,0,1]]))
#print(gagnant_colonne(5,2,[[1,1,2,2,2,1,2],
#                         [2,2,2,1,1,2,1],
#                         [1,1,1,2,2,1,2],
#                         [2,2,1,1,0,2,1],
#                         [1,2,1,0,0,1,2],
#                         [0,2,1,0,0,0,1]]))
#print(dessine_grille([[1,1,2,2,2,1,2],
#                         [2,2,2,1,1,2,1],
#                         [1,1,1,2,2,1,2],
#                         [2,2,1,1,0,2,1],
#                         [1,2,1,0,0,1,2],
#                         [0,2,1,0,0,0,1]]))