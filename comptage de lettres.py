#coding:utf-8
"""
Demander à l'utilisateur de saisir un message
dans ce messaage compter le nombre de fois qu'apparait la lettre "e"

TERMINE
"""
texte = input("Tape ton message ")
x = "e"
i = 0

for y in texte :
    if y == x:
        i = i +1
    else:
        continue

print("ton message contient " + str(i) + " fois la lettre 'e'")





