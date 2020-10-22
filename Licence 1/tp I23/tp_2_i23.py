def Lecture(nomfichier):
    fichier = open(nomfichier,"r")
    liste = fichier.readlines()
    X=set()
    G={}
    Y=set()
    line=0
    for line in liste:
        couple = line.rstrip().split(">")
        if couple[0] not in X:
            X={couple[0]}
        else:
            X=X|{couple[0]}
        if couple[1] not in Y:
            Y={couple[1]}
        else:
            Y=Y|{couple[1]}
        if couple[0]!="" and couple[1]!="":
            if couple[0] in G.keys():
                G[couple[0]]=G[couple[0]]|{couple[1]}
            else:
                G[couple[0]]={couple[1]}
    return (X, G, Y)

def Affiche(c):
    print("X = ",str(c[0]).replace("'",''))
    print("G = ",str(c[1]).replace("'",''))
    print("Y = ",str(c[2]).replace("'",''),end='\n\n')

def reciproque(c):
    G_1 = {}
    for outp in c[2]:
        G_1[outp]=set()
    for inp in c[0]:
        if outp in c[1][inp]:
            G_1[outp].add(inp)
    return C[2],G_1,C[0]

def ImageDirecte(C, A):
    outp = []
    for x in A:
        if x in C[0]:
           outp += [C[1][x]]
        else:
           outp += [{""}]
    return outp

def ImageReciproque(C, B):
    return ImageDirecte(Reciproque(C), B)

def Composer(g, f):
    G_g = g[1]
    G_f = f[1]
    G = dict()
    for inp_g in G_g.keys():
        for outp_g in G_g[inp_g]:
            if len(outp_g) != 0:
                if not inp_g in G.keys():
                    G[inp_g] = set()
                G[inp_g] = ImageDirecte(f, outp_g)[0]
    return g[0], G, f[2]

def EstFonction(c):
    for valeur in c[1].values():
        if len(valeur) > 1:
            return False
    return True


def EstApplication(C):
    if not EstFonction(C): return False
    for entree in C[0]:
        if entree == "": return False
        for sortie in C[1][entree]:
            if len(sortie) == 0:
                return False
    return True

c = Lecture("correspondance.txt")
Comp = Composer(c, Reciproque(c))

Affiche(c)
Affiche(Comp)