from random import randrange
def legal(grille, l, c):
    n,m = len(grille), len(grille[0])
    return 1<=l<n-1 and 1<=c<m-1

def voisinage(grille, lig,col):
    n,m = len(grille), len(grille[0])
    d = [(2,0),(0,2),(-2,0),(0,-2)]
    voisins = []
    for i,j in d:
        l, c= lig+i, col+j
        if legal(grille,l,c):
            voisins.append((l,c))
    return voisins

def frontiere(grille,lig,col):
    voisins =  voisinage(grille,lig,col)
    return [(l,c) for (l,c) in voisins if grille[l][c]==1]

def passage(grille,lig,col):
    voisins =  voisinage(grille,lig,col)
    return [(l,c) for (l,c) in voisins if grille[l][c]==0]

def rand_pop(l):
    if l==[]:
        return None
    i = randrange(len(l))
    l[i],l[-1]=l[-1],l[i]
    return l.pop()

def mid(p,m):
    return ((m[0]+p[0])//2,(m[1]+p[1])//2)

def debut_fin(grille):
    while True:
        i = randrange(len(grille))
        if grille[i][1]==0:
            grille[i][0]=2
            break
    while True:
        i = randrange(len(grille))
        if grille[i][-2]==0:
            grille[i][-1]=3
            break

def prim_maze(la,ha):
    grille = [[1]*la for i in range(ha)]
    lig,col = randrange(0,ha//2)*2+1, randrange(0,la//2)*2+1
    grille[lig][col] = 0
    queue = frontiere(grille,lig,col)
    while queue:
        new = rand_pop(queue)
        voisins = passage(grille,new[0],new[1])
        v = rand_pop(voisins)
        m = mid(v,new)
        grille[new[0]][new[1]] = 0
        grille[m[0]][m[1]] = 0
        for v in frontiere(grille,new[0],new[1]):
            if not (v in queue): 
                queue.append(v)
    debut_fin(grille)
    return grille


if __name__=='__main__':
    la,ha=7,7
    for l in prim_maze(la,ha):
        print(l)
        
