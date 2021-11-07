"""
TERMINE

2 scriptes valides

with open("pi copie.txt", "r") as filin:
    compteur = 0

    for ligne in filin.readlines():
        date = '3'

        if date in ligne:
             compteur=compteur+1

    if compteur > 0:
        print('trouvé', compteur, 'fois')
    else:
        print('non trouvé')
)
"""

# 2 nd code => fonctionne
wanted = " "

c = 0

fichier = open("pi.txt", "r")
for ligne in fichier :
    if wanted in ligne :
        c = c + 1
    else:
        pass
print("le terme cherché est utilisé : ", c, " fois")
fichier.close()

