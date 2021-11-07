"""
En partant de l’exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome
(c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s »

RESOLU

"""

texte = "sos"

lg = len(texte)

for y in texte:

    if texte[0] == texte[-1]:
        valeur = 1

    else:
        valeur = 2

if valeur == 1:
    print("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")
