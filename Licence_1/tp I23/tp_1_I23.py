from random import *

lettres = "abcdefghijklmnopqrstuvwxyz"
parentheses = "()"
operateurs = "!+*"

"""
    Fonction qui sert à lister les variables de l'expression
    rentré en paramètre.

    @param String expression

    @return La liste triée des variables
"""
def ListerVariables(expression):
    variables = []
    for char in expression:
        if char in lettres and not char in variables:
            variables += [char]
    return sorted(variables)


"""
    Fonction qui génère le dictionnaire des variables rentrées
    en paramètre

    @param List variables

    @return Le dictionnaire des variables
"""
def DicoVariables(variables):
    dicovar = {}
    for i, char in enumerate(variables): dicovar[char] = i
    return dicovar


"""
    Fonction qui converti un entier en binaire de n bits.

    @param Integer L'entier
    @param Integer n bits

    @return String Le nombre binaire
"""
def Int2Bin(entier, n):
    binn = bin(entier)[2:]
    if len(binn) < n:
        binn = "0" * (n - len(binn)) + binn
    return binn


"""
    Fonction qui converti un binaire en un tuple de booléens.

    @param String Le binaire

    @return Le tuple de booléens
"""
def Bin2Bool(bits):
    tuple = ()
    for bit in bits:
        tuple += ("True" if bit == "1" else "False",)
    return tuple


"""
    Fonction qui génère un nombre soit égale à 1 soit à 0.

    @return Le nombre 1 ou 0.
"""
def RandBin():
    return False if random() < 0.5 else True


"""
    Fonction qui remplace les !, * et + par respectivement not,
    and et or. Elle remplace aussi les variables par leurs valeurs.

    @param String L'expression
    @param Tuple Les valeurs des variables
    @param Dict Le dictionnaire des variables

    @return L'expression changée
"""
def Math2Python(expression, vecteur, dicovar):
    n_expr = ""
    for char in expression:
        if char == "!": n_expr += "not "
        if char == "*": n_expr += "and"
        if char == "+": n_expr += "or"
        if char == "(": n_expr += "("
        if char == ")": n_expr += ")"
        if char == " ": n_expr += " "
        if char in dicovar:
            n_expr += str(vecteur[dicovar[char]])

    return n_expr


"""
    Fonction qui calcule la table de verité d'une expression.

    @param String L'expression
    @param Dict Les variables
"""
def TableVerite(expression, dicovar):
    n = len(dicovar)

    vecteurs = [(RandBin(), RandBin(), RandBin())]
    len_t = len(vecteurs)
    while len_t < 2**n:
        t = (RandBin(), RandBin(), RandBin())
        if not t in vecteurs: vecteurs += [t]
        len_t = len(vecteurs)

    result = []
    for vecteur in vecteurs:
        result += [vecteur + (eval(Math2Python(expression, vecteur, dicovar)),)]

    return result


"""
    Fonction qui affiche la table de verité dans la console.

    @param Dict Les variables
    @param String L'expression
    @param List<Tuple> Liste des lignes du tableau
"""
def AfficheTableVerite(dicovar, expression, result):
    line_1 = "| " + " | ".join(list(sorted(dicovar.keys())) + [expression])  + " |"
    line_a = "—" * len(line_1)

    print("\n" + line_a)
    print(line_1)
    print(line_a)

    for i in range(len(result)):
        v = ["1" if v else "0" for v in sorted(result)[i]]
        print("| " + " | ".join(v))

    print(line_a + "\n")


def FNC(TDV, listevar):
    pass

def FND(TDV, listevar):
    pass



expression = "!(p + q) * (!p + r) + (p * q)"

variables = ListerVariables(expression)
dicovar = DicoVariables(variables)
result = TableVerite(expression, dicovar)
AfficheTableVerite(dicovar, expression, result)

print (variables)
print (dicovar)
print(result)
print (Int2Bin(5,5))
print (Bin2Bool(Int2Bin(5,5)))
print(result)
print (AfficheTableVerite)
