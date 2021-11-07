"""
écrire une fonction "ordonne" qui prend une chaîne de caractères (string) et retourne ce même string mais en
l'ordonnant par ordre alphabétique.

résolu
"""

def ordonne() :
    ch = input("taper le message")
    x = list(ch)
    print("l'ensemble de départ est : ", ch)
    y = sorted(x)
    stry = "".join(y)
    print("L'ensemble d'arrivée est :", stry)

ordonne()