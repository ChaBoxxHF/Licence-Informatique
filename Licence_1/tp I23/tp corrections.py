#####################################################
# CORRECTION TP1 (MATHEMATIQUES POUR L'INFORMATIQUE)
#
# NB. Rappeler aux Ã©tudiants que les listes et
# dictionnaires sont mutables mais pas les chaÃ®nes
# ni les tuples. D'autre part les listes Ã©tant des
# rÃ©fÃ©rences, les changements sur les valeurs d'une
# liste dans une fonction restent effectives sur la
# liste d'appel.
#####################################################

#-----------------------------------------------------
# Echange les valeurs aux indices i et j dans une
# structure Ã©numÃ©rÃ©e mutable. Didactique pour Ã©viter 
# l'emploi de x,y = y,x spÃ©cifique au Python et qui
# donne de mauvaises habitudes de programmation.
#-----------------------------------------------------
def Echanger(L,i,j):
    aux = L[i]
    L[i] = L[j]
    L[j] = aux
    return L

#-----------------------------------------------------
# Principe fondateur du tri Ã  bulles:
# Fait remonter la plus grande valeur de l'intervalle
# [i,j] de la liste L en position j en comparant les
# termes d'indices k et k + 1 pour k allant de i Ã 
# j - 1
#-----------------------------------------------------
def Propager(L,i,j):
    k = i
    while k < j:
        if L[k] > L[k + 1]:
            Echanger(L,k,k+1)
        k = k + 1
    return L

#-----------------------------------------------------
# Algorithme du tri Ã  bulles
#-----------------------------------------------------
def TriBulles(L):
    d = len(L) - 1
    while (d > 0):
        Propager(L,0,d)
        d = d - 1
    return L

#-----------------------------------------------------
# Extraction des variables boolÃ©ennes
# (Sans prÃ©occupation d'efficacitÃ©...)
#-----------------------------------------------------
#def ListerVariables(expression):
#    variables = []
#    lexique = "abcdefghijklmnopqrstuvwxyz"
#    for symbole in expression:
#        if (symbole in lexique) and not (symbole in variables):
#            variables.append(symbole)
#    return variables

#-----------------------------------------------------
# Extraction des variables boolÃ©ennes.
# Plus efficace, utilise les types adaptÃ©s.
#-----------------------------------------------------
def ListerVariables(expression):
    variables = set()
    for symbole in expression.lower():
        if symbole.isalpha():
            variables.add(symbole)
    return list(variables)

#-----------------------------------------------------
# Construction du dictionnaire Ã  partir de la liste
# des variables
#-----------------------------------------------------
def DicoVariables(liste):
    dico = {}
    i = 0
    while i < len(liste):
        dico[liste[i]] = i
        i = i + 1
    return dico

#-----------------------------------------------------
# Convertit un entier en binaire sur n bits en
# complÃ©tant par des 0 Ã  gauche si sa reprÃ©sentation
# comport moins de n bits
#----------------------------------------------------
def Int2Bin(entier,n):
    bits = bin(entier)[2:]
    if len(bits) < n:
        bits = "0" * (n - len(bits)) + bits
    return bits
        
#-----------------------------------------------------
# Conversion d'une chaÃ®ne de caractÃ¨res de 0 ou 1
# en le tuple de boolÃ©ens correspondant.
#-----------------------------------------------------
def Bin2Bool(bits):
    booleens  = ()
    for b in bits:
        booleens = booleens + (b == "1",)
    return booleens

#-----------------------------------------------------
# Convertit une expression logique formelle en 
# expression Ã©quivalente du langage Python.
#-----------------------------------------------------
def Math2Python(expression,vecteur,dicovar):
    pexp = ""
    operateurs = {"!":" not ","*":" and ","+":" or "}
    for symb in expression:
        if symb in dicovar.keys():
            pexp = pexp + str(vecteur[dicovar[symb]])
        elif symb in operateurs.keys():
            pexp = pexp + operateurs[symb]
        else:
            pexp = pexp + symb
    return pexp

#-------------------------------------------------------
# Renvoie la table de vÃ©ritÃ© de l'expression passee en
# parametre sous forme de liste contenant les 2^n valeurs
# possibles de l'expression de n variables logiques. 
#-------------------------------------------------------
def TableVerite(expression,dicovar):
    nbvar = len(dicovar.keys())
    TDV = [0] * (2**nbvar)
    for entier in range(2**nbvar):
        vecteur = Bin2Bool(Int2Bin(entier,nbvar))
        chaine = Math2Python(expression,vecteur,dicovar)
        if eval(chaine):
            TDV[entier] = 1
    return TDV

#--------------------------------------------------------
# Formate la sortie de l'Ã©valuation de l'expression
# pour un tuple logique de nbvar variables codÃ© sous
# forme d'entier
#--------------------------------------------------------
def AfficherLigne(entier,nbvar,TDV):
    for bit in Int2Bin(entier,nbvar):
        print(bit.rjust(2), end='')       
    print(' |' + str(TDV[entier]).rjust(2))

#-------------------------------------------------------
# Affiche la table de vÃ©ritÃ© de l'expression boolÃ©enne
#-------------------------------------------------------
def AfficherTDV(TDV,dicovar):
    nbvar = len(dicovar.keys())
    for v in sorted(dicovar.keys()):
        print(v.rjust(2),end='')
    print(" | E".rjust(2))
    for entier in range(2**nbvar):
        AfficherLigne(entier,nbvar,TDV)

#-------------------------------------------------------
# Renvoie la FND d'une expression Ã  partir de sa table de
# vÃ©ritÃ©. 
#-------------------------------------------------------     
def FND(TDV,listevar):
    n = len(listevar)
    debut = True
    print("FND = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 1):
            bits = Int2Bin(entier,n)
            if debut:
                debut = False
            else:
                print(" + ",end='')
            i = 0
            while i < n:
                if bits[i] == "1":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
        entier = entier + 1
    print()

#-------------------------------------------------------
# Renvoie la FNC d'une expression Ã  partir de sa table de
# vÃ©ritÃ©. 
#-------------------------------------------------------     
def FNC(TDV,listevar):
    n = len(listevar)
    print("FNC = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 0):
            bits = Int2Bin(entier,n)
            debut = True
            i = 0
            while i < n:
                if debut:
                    print('(', end='')
                    debut = False
                else:
                    print("+", end='')
                if bits[i] == "0":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
            print(')',end='')
        entier = entier + 1
    print()
        
##########################################################
# PROGRAMME PRINCIPAL
##########################################################
expression = input("Expression = ")
listevar = ListerVariables(expression)
print(listevar)
listevar = TriBulles(listevar)
print(listevar)
dicovar = DicoVariables(listevar)
print(dicovar)
TDV = TableVerite(expression,dicovar)
AfficherTDV(TDV,dicovar)
FND(TDV,listevar)
FNC(TDV,listevar)


#####################################################
#
# CORRECTION TP2 (MATHEMATIQUES POUR L'INFORMATIQUE)
#
#
#####################################################

import sys

#-----------------------------------------------------
# Renvoie une correspondance (X,G,Y) codÃ©e en tuple
# Python Ã  partir d'un fichier dont chaque ligne
# contient un couple (x,y) codÃ© par la chaÃ®ne x>y.
# une chaÃ®ne >y sans x dÃ©signe un terme de Y qui n'a
# pas de correspondant dans X, une chaine x> sans y
# dÃ©signe un terme de X qui n'a pas de correspondant
# dans Y.
# X et Y sont des "set" Python, alors que G est un
# dictionnaire dont les clefs sont le domaine de
# dÃ©finition de la correspondance et G[x] est
# l'image de x sous forme de "set" Python.
#-----------------------------------------------------
def Lecture(nomfichier):
    fichier = open(nomfichier,"r")
    liste = fichier.readlines()
    X = set()
    Y = set()
    G = {}
    for fleche in liste:
        couple = fleche.rstrip().split(">")
        x,y = couple[0],couple[1]
        # on s'assure de ne pas rajouter la chaÃ®ne vide
        # dans les ensembles de dÃ©part et d'arrivÃ©e
        if x != '':
            X = X | {x}
        if y != '':
            Y = Y | {y}
        # si la fleche relie bien deux objets
        # on rajoute le couple dans le graphe
        if (x != '') and (y != ''):
            if (x in G.keys()):
                G[x] = G[x] | {y}
            else:
                G[x] = {y}
    return (X,G,Y)

#---------------------------------------------------------------
# Renvoie la correspondance rÃ©ciproque.
#---------------------------------------------------------------
def Reciproque(correspondance):
    X,G,Y = correspondance[0],correspondance[1],correspondance[2]
    GR = {}
    for x in G.keys():        
        for y in G[x]:
            if y in GI.keys():                
                GR[y] = GR[y] | {x}
            else:
                GR[y] = {x}
    return (Y,GR,X)

#---------------------------------------------------------------
# Renvoie l'image directe d'une partie A pour la correspondance
# (X,G,Y). On suppose que A est un sous-ensemble de X pour ne
# pas polluer le script avec des tests inutiles.
#---------------------------------------------------------------
def ImageDirecte(correspondance,A):
    X,G,Y = correspondance[0],correspondance[1],correspondance[2]
    IDA = set()
    for x in G.keys():
        if x in A:
            IDA = IDA | G[x]
    return IDA

#---------------------------------------------------------------
# Renvoie l'image rÃ©ciproque d'une partie B pour la correspondance
# (X,G,Y) On suppose que B est un sous-ensemble de Y pour ne
# pas pollue le script avec des tests inutiles.
#---------------------------------------------------------------
def ImageReciproque(correspondance,B):
    creciproque = Reciproque(correspondance)
    return ImageDirecte(creciproque,B)

#---------------------------------------------------------------
# Renvoie la correspondance g o f, composÃ©e des deux
# correspondances f:X->Y et g:Y->Z.
#---------------------------------------------------------------
def Composer(g,f):    
    (X,Gf,Y) = (f[0],f[1],f[2])
    (Gg,Z) = (g[1],g[2])
    Ggof = {}
    for x in Gf.keys():
        for y in Gf[x]:
            if y in Gg.keys():
                if x in Ggof.keys():
                    Ggof[x] = Ggof[x] | Gg[y] 
                else:
                    Ggof[x] = Gg[y]
    return (X,Ggof,Z)

#---------------------------------------------------------------
# DÃ©cide si une correspondance est une fonction   
#---------------------------------------------------------------
def EstFonction(correspondance):
    (X,G,Y) = (correspondance[0],correspondance[1],correspondance[2])
    retour = True
    for x in G.keys():
        if (len(G[x]) > 1):
            retour = False
            break    
    return retour

#---------------------------------------------------------------
# DÃ©cide si une correspondance est une application
#---------------------------------------------------------------
def EstApplication(correspondance):
    (X,G,Y) = (correspondance[0],correspondance[1],correspondance[2])
    retour = True
    for x in X:
        if ((not x in G.keys()) or (len(G[x]) > 1)):
            retour = False
            break    
    return retour

#---------------------------------------------------------------
# Affiche une correspondance plus lisiblement qu'un simple print
#---------------------------------------------------------------
def Affiche(correspondance):
    print("X = ",str(correspondance[0]).replace("'",''))
    print("G = ",str(correspondance[1]).replace("'",''))
    print("Y = ",str(correspondance[2]).replace("'",''),end='\n\n')

##########################################################
# PROGRAMME PRINCIPAL
##########################################################
nomfichier = input("Correspondance f : ")
f = Lecture(nomfichier)
nomfichier = input("Correspondance g : ")
g = Lecture(nomfichier)
Affiche(f)
Affiche(g)
rf = Reciproque(f)
Affiche(rf)
gof = Composer(rf,f)
Affiche(gof)
gof = Composer(g,f)
Affiche(gof)


#####################################################
#
# CORRECTION TP3 (MATHEMATIQUES POUR L'INFORMATIQUE)
# Quelques variations autour de la combinatoire.
#
###################################################

#------------------------------------------------------------------------
# Renvoie la factorielle de l'entier passÃ© en paramÃ¨tre
# Exemple typique de la fonction qu'IL NE FAUT PAS Ã©crire rÃ©cursivement.
# En effet, conserver les calculs intermÃ©diaires dans une pile ne
# sert Ã  rien ici, mÃªme pas pour simplifier l'Ã©criture de l'algo.
#------------------------------------------------------------------------
def factorielle(n):
    retour = 1
    for i in range(2,n+1):
        retour = retour * i
    return retour

#------------------------------------------------------------------------
# Renvoie la liste des n+1 coefficients binomiaux C(n,p) sur la derniÃ¨re 
# ligne du triangle de Pascal.
#------------------------------------------------------------------------
def TrianglePascal(n):
    TP = [0] * (n + 1)
    TP[0] = 1
    for k in range(1,n + 1):
        for i in range(k):
            TP[k - i] = TP[k - i] + TP[k - i - 1]
    return TP

#------------------------------------------------------------------------
# Renvoie la liste des codes phoque de longueur n. Version rÃ©cursive
# Base rÃ©currente: si n = 0, n=1 ou n=2 (if et elifs)
# autodÃ©finition: n > 2 (else)
#------------------------------------------------------------------------
def phoque(n):
    if n == 0:
        return []
    elif n == 1:
        return ['.']
    elif n == 2:
        return ['..','-']
    else:
        return [ '.' + x for x in phoque(n-1)] + [ '-' + x for x in phoque(n-2)]

#------------------------------------------------------------------------
# Renvoie la liste des codes phoque de longueur n. Version itÃ©rative
#------------------------------------------------------------------------
def phoqueit(n):
    A = ['.']
    B = ['..','-']
    if n == 0:
        L = [0]
    elif n == 1:
        L = A
    elif n == 2:
        L = B
    else:
        for k in range(3,n+1):
            L = ['.' + x for x in B] + ['-' + x for x in A]
            A = B
            B = L
    return L

#------------------------------------------------------------------------
# Renvoie les n+1 premiers termes de la suite de Fibonacci dÃ©finie par
# F_{n+2} := F_{n+1} + F_{n} avec F_0:=0 et F_1:=1
# Ne DOIT PAS s'Ã©crire rÃ©cursivement, il n'y a que deux termes Ã 
# garder en mÃ©moire pour calculer le suivant et pas tout l'historique
# de la pile !
#------------------------------------------------------------------------
def Fibonacci(n):
    F = (0,1)
    for k in range(2,n+1):
        F = F + (F[k-1]+F[k-2],)
    return F

#------------------------------------------------------------------------
# Affiche tous les Ã©lÃ©ments de l'ensemble [1,m]^n (n-uplets)
#------------------------------------------------------------------------
def genuplet(n,m,nuplet):
    if (n == 0):
        print(nuplet)
    else:
        for i in range(m):
            genuplet(n-1, m, nuplet + (i+1,))

#########################################################################
# PROGRAMME PRINCIPAL
#########################################################################

n = int(input("Ordre n = "))
print('Coefficients binomiaux :',TrianglePascal(n))
print('Codes phoque de longueur',n-1,':',phoqueit(n-1))
print(Fibonacci(n))
n = int(input("Dimension n  = "))
m = int(input("Valeur max m = "))
genuplet(n,m,())


#########################################################
#
# CORRECTION TP4 (MATHEMATIQUES POUR L'INFORMATIQUE)
# Quelques variations autour du groupe des permutations
#
#########################################################

#------------------------------------------------------------------------
# Convertit la chaÃ®ne lue au clavier par un tuple d'entiers
# Ne vÃ©rifie pas s'il s'agit d'une permutation.
#------------------------------------------------------------------------
def Lire():
   chaine = input("Permutation = ")
   return tuple([int(x) - 1 for x in chaine.split()])

#------------------------------------------------------------------------
# Affiche une permutation en rajoutant 1 aux valeurs du tuple qui
# la code.
#------------------------------------------------------------------------
def Ecrire(s):
    print('(',end='')
    for i in range(len(s) - 1):
        print(s[i] + 1, end=',')
    print(s[len(s) - 1] + 1,end=')\n')
    
#------------------------------------------------------------------------
# DÃ©cide si un tuple d'entier est code une permutation.
# PlutÃ´t que de chercher pour chaque entier i dans [1,n] s'il est
# dans le tuple s (de longueur n) occasionnant ainsi n balayages de
# ce tuple, on crÃ©e une liste B de n boolÃ©ens initialisÃ©s Ã  False
# qui indique si chaque valeur appartient ou non Ã  la permutation
#------------------------------------------------------------------------
def EstPermutation(s):
    n = len(s)
    B = [False] * n
    for i in s:
        if (i >= 0) and (i < n):
            # on met Ã  jour si nÃ©cessaire les boolÃ©ens de B
            # si la valeur courante est bien dans [1,n]            
            B[i] = True            
        else:
            # sinon on sait dÃ©jÃ  que ce n'est pas une perm.
            return False
    i = 0
    while (i < n):
        # on balaie cette fois B pour s'assurer que
        # toutes les valeurs de [0,n-1] sont prÃ©sentes dans s
        if not B[i]:
            return False
        i = i + 1
    return True
    
#------------------------------------------------------------------------
# Renvoie la permutation inverse de celle passÃ©e en parametre s et
# codÃ©e sous forme de tuple s:=(s(1),s(2),...,s(n)).
# NB. Les tuples Ã©tant non-mutables, il est prÃ©fÃ©rable de crÃ©er d'abord
# une liste afin d'Ã©viter de balayer le tuple s pour ajouter le prochain
# terme du tuple rÃ©sultat.
#------------------------------------------------------------------------
def Inverser(s):
    retour = [0] * len(s)
    for i in range(len(s)):
        retour[s[i]] = i
    return tuple(retour)

#------------------------------------------------------------------------
# Renvoie la composition sÂ°t des deux permutations s et t passÃ©es
# en paramÃ¨tre. On suppose bien sÃ»r qu'il s'agit de deux permutations de
# mÃªme longueur.
#------------------------------------------------------------------------
def Composer(s,t):
    c = ()
    for i in range(len(s)):
        c = c + (t[s[i]],)
    return c

#------------------------------------------------------------------------
# Renvoie l'orbite de k suivant la permutation s
#------------------------------------------------------------------------
def Orbite(k,s):
   k = k - 1
   debut = k
   o = (k,)
   while (s[k] != debut):
      k = s[k]
      o = o + (k,)
   return o

#------------------------------------------------------------------------
# Renvoie le plus petit indice j > i tel que B[j] ou -1 s'il n'y en a pas
#------------------------------------------------------------------------
def Suivant(B,i):
   j = i + 1
   retour = -1
   while (j < len(B)) and (not B[j]):
      j = j + 1
   if (j < len(B)):
      retour = j        
   return retour

#------------------------------------------------------------------------
# Renvoie la dÃ©composition de s en produit de cycles Ã  supports
# disjoints. On crÃ©e une liste B de n boolÃ©ens (permutation de S_n)
# qui indique si oui ou non l'entier i a dÃ©jÃ  Ã©tÃ© inclus dans un
# cycle.
#------------------------------------------------------------------------
def Cycles(s):
   n = len(s)
   B = [True] * n
   i = 0
   produitcycles = ()
   while (i != -1):
      # tant qu'il reste des elements non collectÃ©s dans les
      # prÃ©cÃ©dents cycles, on initialise le nouveau cycle avec i
      cycle = (i,)
      B[i] = False
      debut = i
      while (s[i] != debut):
         cycle = cycle + (s[i],)
         i = s[i]
         B[i] = False
      if (len(cycle) > 1):
         # on ne conserve que les orbites de plus d'un Ã©lÃ©ment
         produitcycles = produitcycles + (cycle,)
      i = Suivant(B,i)
   return produitcycles

#------------------------------------------------------------------------
# Renvoie la dÃ©composition de s en produit de transpositions.
# S'appuie sur la dÃ©composition en produit de cycles et la preuve
# constructive du thÃ©orÃ¨me 29. Ex: (a,b,c) = (a,b)(b,c)
#------------------------------------------------------------------------
def Transpositions(s):
   produitcycles = Cycles(s)
   produittransp = ()
   for cycle in produitcycles:
      i = 0
      while i < len(cycle) - 1:
         produittransp = produittransp + ((cycle[i],cycle[i+1]),)
         i = i + 1
   return produittransp

#------------------------------------------------------------------------
# Renvoie la signature d'une permutation. Il faut recalculer le nombre
# d'orbites rÃ©duites Ã  un singleton. C'est
#------------------------------------------------------------------------
def signature(s):
   produitcycles = Cycles(s)
   somme = len(produitcycles)
   for cycle in produitcycles:
      somme = somme - len(cycle)
   return int((-1)**(somme))

#------------------------------------------------------------------------
# Renvoie la conjuguÃ©e de la permutation s par r
#------------------------------------------------------------------------
def Conjuguer(s,r):
   return Composer(r,Composer(s,Inverser(r)))


##########################################################################
# PROGRAMME PRINCIPAL
##########################################################################
s = Lire()
print(EstPermutation(s))
Ecrire(s)
#Ecrire(Inverser(s))
#print(Composer(s,t))
PC = Cycles(s)
print("Cycles:")
for i in range(len(PC)):
    Ecrire(PC[i])
PT = Transpositions(s)
print("Transpositions:")
for i in range(len(PT)):
    Ecrire(PT[i])
print("Signature: ",end='')
print(signature(s))
Ecrire(Orbite(1,s))
#Ecrire(Conjuguer(s,s))


#########################################################
#
# CORRECTION TP5 (MATHEMATIQUES POUR L'INFORMATIQUE)
# Quelques variations autour de l'arithmÃ©tique
#
#########################################################

#------------------------------------------------------------------------
# Renvoie le chiffrÃ© de Cesar, on suppose que les lettres du clair sont
# toutes en majuscules.
# NB. Les codes des lettres respectent l'ordre alphabÃ©tique. En
# soustrayant par ord("A"), on ramÃ¨ne tous les codes des lettres
# majuscules dans l'intervalle [0,25] pour pouvoir calculer modulo 26.
#------------------------------------------------------------------------
def Chiffrer(clair,clef):
   chiffre = ""
   for lettre in clair:
      oldcode = ord(lettre) - ord("A")
      newcode = (oldcode + clef) % 26
      newlettre = chr(ord("A") + newcode)
      chiffre = chiffre + newlettre
   return chiffre

#------------------------------------------------------------------------
# Renvoie la liste (sous forme de tuple) des nombres premiers infÃ©rieurs
# Ã  N avec l'algorithme du crible d'EratosthÃ¨ne.
# On crÃ©e une liste "EstPremier" de (N+1) boolÃ©ens indiquant si l'indice est
# premier ou non. 
#------------------------------------------------------------------------
def Cribler(N):
   EstPremier = (N + 1) * [True]
   EstPremier[0] = False
   EstPremier[1] = False
   p = 1
   while ((p * p) <= N):
      p = p + 1
      while (((p * p) <= N) and (not(EstPremier[p]))):
         p = p + 1
      k = 2
      while (k * p <= N):
         EstPremier[k * p] = False
         k = k + 1
   premiers = ()   
   # On collecte uniquement les nombres premiers
   for k in range(2,N+1):
      if EstPremier[k]:
         premiers = premiers + (k,)
   return premiers

#------------------------------------------------------------------------
# Renvoie la liste (sous forme de tuple) des facteurs premiers de N
# C'est l'algorithme naÃ¯f qui est employÃ©
#------------------------------------------------------------------------
def Factoriser(N):
   p = 2
   facteurs = ()
   while (N % p == 0):
      facteurs = facteurs + (p,)
      N = N // p
   p = 3
   while (p*p <= N):
      while (N % p == 0):
         facteurs = facteurs + (p,)
         N = N // p
      p = p + 2
   if (N != 1):
      facteurs = facteurs + (N,)
   return facteurs

#------------------------------------------------------------------------
# Renvoie la table d'addition ou de multiplication de Z/nZ
#------------------------------------------------------------------------
def Table(n,op):
   T = ()
   for a in range(1,n):
      Ta = ()
      for b in range(1,n):
         exp = "(" + str(a) + op + str(b) + ") % " + str(n)
         Ta = Ta + (eval(exp),)
      T = T + (Ta,)
   return T

#------------------------------------------------------------------------
# Formatte l'affichage d'une table
#------------------------------------------------------------------------
def AfficheTable(T):
   for ligne in T:
      for x in ligne:
         print(str(x).rjust(3),end='')
      print()

#------------------------------------------------------------------------
# Renvoie l'image d'un entier dans Z/9Z en utilisant le critÃ¨re de
# divisibilitÃ© par 9. Calcule la somme des chiffres (et recommence si
# le nombre obtenu a plus d'un chiffre)
#------------------------------------------------------------------------
def mod9(N):
   chiffres = str(N)
   while len(chiffres) > 1:
      N = 0
      for c in chiffres:
         N = N + int(c)
      chiffres = str(N)
   if N == 9:
      N = 0
   return N 

#------------------------------------------------------------------------
# Renvoie un couple (u,v) solution de l'Ã©quation au + bv = d
# oÃ¹ d = PGCD(a,b) avec l'algorithme d'Euclide Ã©tendu.
# NB. La liste des quotients contient un quotient de plus, on dÃ©marre
# donc Ã  l'avant dernier terme. Attention en algorithmique la liste Q
# est indexÃ©e de 1 Ã  n, pas en Python (d'oÃ¹ le - 2).
#------------------------------------------------------------------------
def Euclide(a,b):
   Q = []
   while b > 0:
      Q = Q + [a // b]
      t = b
      b = a % b
      a = t
      # affichage des quotients   
      # print(Q)
   u = 0
   v = 1
   i = len(Q) - 2
   while (i >= 0):
      t = u
      u = v
      v = t - Q[i] * v
      i = i - 1
   return (u,v)

##########################################################################
# PROGRAMME PRINCIPAL
##########################################################################
clef = int(input("Clef de CÃ©sar = "))
print(Chiffrer(Chiffrer("JEFAISUNESSAI",clef),26-clef))

print("\n")
print(Cribler(100))

print("\n")
print(Factoriser(32))

print("\n")
AfficheTable(Table(12,"+"))

print("\n")
AfficheTable(Table(12,"*"))

print("\n");
print(mod9(19))

print("\n");
print(Euclide(192,57))
