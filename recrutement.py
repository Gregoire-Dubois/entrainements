"""
script simulateur d'embauche
1) générer une valeur aléatoire entre 0 et 10
2) demander à l'utilsateur d'entrer une valeur entre 0 et 10
    si le nombre est identique == boulot décroché
    si le nombre est différent == pas le boulot

faire une boucle tant que le candidat veut percévérer
"""
from random import randint

q="" #variable question
n=0 #variable nombre donné par l'utilisateur
x=0 #variable nombre aléatoire

c=True #

while c:
    x=randint(0, 11) #génère un entier entre allant de 0 a 10
    print("Entrez le niveau d'adéquation du candidat. Niveau allant de 0 et 10 inclus")

    try:
        n = input("Niveau d'adéquation du candidat : ")
        if int(n) <0 or int(n)>10:
            print("Seuls des nombres entiers de 0 et 10 inclus sont attendus")
        else:
            if int(n) == x:
                print("vous êtes recruté")
                break
                print("Fin de programme")
            else:
                print("Ca ne sera pas pour cette fois. Percévérer ?")
                q = input("Percévérer ? oui ou non ?")
                if q == "non":
                    c = False
    except ValueError:
        print("La valeur attendue ne peut etre qu'un nombre entier")
