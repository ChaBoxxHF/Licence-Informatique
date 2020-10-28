def PythonLecture(f):
    fichier = open(f,"r")
    liste = fichier.readlines()
    i = 0
    X = set()
    Y = set()
    G = {}
    while i<len(liste):
        couple=liste[i].rstrip().split(">")
        x=couple[0]
        y=couple[1]
        if couple[0] not in X and x !="":
            X = X | {couple[0],}
        if couple[1] not in Y and y!="":
            Y=Y|{y,}
        if x!="" and y!="":
            if x in G.keys():
                G[x]=G[x]|{y}
        else:
            G[x]={y}
        i+=1
    return(X,Y,G)

def reciproque(f):
    fichier = open(f,"r")
    liste = fichier.readlines()
    i = 0
    X = set()
    Y = set()
    G = {}
    while i<len(liste):
        couple=liste[i].rstrip().split(">")
        x=couple[0]
        y=couple[1]
        if couple[0] not in X and x !="":
            X = X | {couple[0],}
        if y not in Y and y != "":
            Y = Y |{couple[1],}
        if x != "" and y != "":
            if y in G.keys():
                G[y]=G[y]|{x}
            else:
                G[y]={x}
        i+=1
    return(X,Y,G)

def imgdirect(C,A):
    G = C[2]
    L=set()
    for i in G:
        for el in G[i]:
            if el in A:
                if el not in L:
                    L = L + el
    return L


def imagerecip(C,B):
    G = C[2]
    L=set()
    for i in G:
        for el in G[i]:
            if el in B:
                if el not in L:
                    L = L + el
    return L
