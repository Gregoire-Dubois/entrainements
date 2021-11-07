"""
Ecrire un programme qui sélectionne aléatoirement un chiffre compris en 0 et 100

demander à l'utilisateur de deviner le chiffre

ajouter par la suite un compteur pour limiter les tentatives à 3 essaies

"""
import random

x = random.randint(0,100)
print(x)
y = 0
c = 0

while y != "":
    c = c + 1
    if c <= 4 :
        y = int(input("saisissez un nombre compris entre 0 et 100"))
        if y == x :
            if c <= 1 :
                print("Félicitation, le nombre ", x, " était la bonne réponse")
                print("Tu as trouvé le chiffre mystère avec ", c, " tentative")
            elif c > 1 :
                print("Félicitation, le nombre " , x, " était la bonne réponse")
                print("Tu as trouvé le chiffre mystère avec ", c, " tentative(s)")
            break
        elif y < x :
            print("Le chiffre cherché est plus grand")
        elif y > x :
            print("Le chiffre cherché est plus petit")
    else:
        print("Arf pas de chance retente ta chance une autre fois")
        break