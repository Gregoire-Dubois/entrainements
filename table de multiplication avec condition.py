"""
Avec la table de multiplication de 13, afficher les 500 premiers résultats et indiquer s'ils sont multiples de 7
Les multiples de 7 sont affichés avec le symbole *

"""

table = 13
i = 0

while i < 500 :
    i = i+1
    resultat = table * i
    if resultat %7 == 0 :
        print(str(resultat) + " *")
    else:
        print(str(resultat))
